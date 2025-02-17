"""
Application entrypoint
"""
import asyncio
import logging
from livekit import rtc
from livekit.agents import llm, AutoSubscribe, metrics
from livekit.agents import WorkerOptions, cli, JobContext
from livekit_playground.agent.agent import create_agent, prewarm

logger = logging.getLogger("voice-assistant")

async def entrypoint(ctx: JobContext):
    try:
        # Initialize chat context
        initial_ctx = llm.ChatContext().append(
            role="system",
            text="You are a voice assistant created by LiveKit. Your interface with users will be voice. "
                 "You should use short and concise responses, and avoiding usage of unpronounceable punctuation."
        )

        logger.info(f"connecting to room {ctx.room.name}")
        await ctx.connect(auto_subscribe=AutoSubscribe.AUDIO_ONLY)

        # Wait for participant
        participant = await ctx.wait_for_participant()
        if not participant:
            logger.error("No participant joined the room")
            return
            
        logger.info(f"starting voice assistant for participant {participant.identity}")

        # Create and start the agent
        try:
            agent = await create_agent(ctx, initial_ctx)
            agent.start(ctx.room, participant)
        except Exception as e:
            logger.error(f"Failed to create or start agent: {str(e)}")
            return

        # Set up usage collection
        usage_collector = metrics.UsageCollector()

        @agent.on("metrics_collected")
        def on_metrics_collected(agent_metrics: metrics.AgentMetrics):
            metrics.log_metrics(agent_metrics)
            usage_collector.collect(agent_metrics)

        async def log_usage():
            summary = usage_collector.get_summary()
            logger.info(f"Usage: ${summary}")

        ctx.add_shutdown_callback(log_usage)

        # Handle chat messages
        chat = rtc.ChatManager(ctx.room)

        async def answer_from_text(txt: str):
            chat_ctx = agent.chat_ctx.copy()
            chat_ctx.append(role="user", text=txt)
            stream = agent.llm.chat(chat_ctx=chat_ctx)
            await agent.say(stream)

        @chat.on("message_received")
        def on_chat_received(msg: rtc.ChatMessage):
            if msg.message:
                asyncio.create_task(answer_from_text(msg.message))

        # Initial greeting
        await agent.say("Hey, how can I help you today?", allow_interruptions=True)

    except Exception as e:
        logger.error(f"Error in entrypoint: {str(e)}")
        raise

if __name__ == "__main__":
    cli.run_app(
        WorkerOptions(
            entrypoint_fnc=entrypoint,
            prewarm_fnc=prewarm,
            num_idle_processes=2
        ),
    )
