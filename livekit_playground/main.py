# Modified agent.py
import logging
from livekit.plugins import silero
from livekit.agents import JobContext, JobProcess, cli, metrics
from livekit_playground.agent.agent import create_agent
from livekit_playground.agent.context import create_initial_context
from livekit_playground.agent.options import create_worker_options

def prewarm(proc: JobProcess):
    proc.userdata["vad"] = silero.VAD.load()

async def entrypoint(ctx: JobContext):
    print("entrypoint")
    initial_ctx = create_initial_context()

    # Create the agent instance but don't start it yet
    agent = await create_agent(ctx, initial_ctx)
    usage_collector = metrics.UsageCollector()

    @agent.on("metrics_collected")
    def on_metrics_collected(agent_metrics: metrics.AgentMetrics):
        metrics.log_metrics(agent_metrics)
        usage_collector.collect(agent_metrics)

    # Wait for dispatch signal (room assignment)
    logging.info(f"Waiting for room assignment...")
    await ctx.wait_for_dispatch()

    logging.info(f"Connecting to room {ctx.room.name}")
    await ctx.connect()

    # Wait for the first participant
    participant = await ctx.wait_for_participant()
    logging.info(f"Starting voice assistant for participant {participant.identity}")

    # Start the agent
    # agent.start(ctx.room, participant)
    # await agent.say("Hello, my name is Elena. How can I help you today?", allow_interruptions=True)

if __name__ == "__main__":
    cli.run_app(create_worker_options(prewarm_fnc=prewarm, entrypoint_fnc=entrypoint))
