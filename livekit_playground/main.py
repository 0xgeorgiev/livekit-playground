"""
Main entrypoint for the assistant
"""
import logging
from livekit.plugins import silero
from livekit.agents import JobContext, JobProcess, AutoSubscribe, cli, metrics
from livekit_playground.assistant.assistant import create_assistant
from livekit_playground.assistant.contexts import create_initial_inbound_context
from livekit_playground.assistant.options import create_worker_options

def prewarm(proc: JobProcess):
    """
    Load the VAD model into the userdata of the process
    """
    proc.userdata["vad"] = silero.VAD.load()

async def entrypoint(ctx: JobContext):
    """
    Entrypoint for the assistant.
    Executed when the worker is assigned to a room.
    """
    # Create the initial chat context
    initial_chat_ctx = create_initial_inbound_context()
    # Connect to the room with audio only
    await ctx.connect(auto_subscribe=AutoSubscribe.AUDIO_ONLY)
    # Create the assistant instance
    assistant = await create_assistant(ctx=ctx, initial_ctx=initial_chat_ctx)
    # Gather usage metrics
    usage_collector = metrics.UsageCollector()

    @assistant.on("metrics_collected")
    def on_metrics_collected(agent_metrics: metrics.AgentMetrics):
        """
        Collect and log metrics
        """
        metrics.log_metrics(agent_metrics)
        usage_collector.collect(agent_metrics)
        
    # Add usage summary logging on shutdown
    async def log_usage():
        summary = usage_collector.get_summary()
        logging.info(f"Session Usage Summary: {summary}")

    ctx.add_shutdown_callback(log_usage)
    
    # Start the assistant
    assistant.start(ctx.room)

if __name__ == "__main__":
    cli.run_app(create_worker_options(prewarm_fnc=prewarm, entrypoint_fnc=entrypoint))
