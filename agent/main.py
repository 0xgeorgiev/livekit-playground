"""
Main entrypoint for the assistant
"""
from livekit.plugins import silero
from livekit.agents import JobContext, JobProcess, AutoSubscribe, cli
from agent.assistant.voice_pipeline_agent import create_assistant
from agent.assistant.context import get_outbound_noshow_agent_context
from agent.worker_options import create_worker_options

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
    # Create the initial chat context (no-show outbound agent)
    initial_chat_ctx = get_outbound_noshow_agent_context()
    
    # Connect to the room with audio only
    await ctx.connect(auto_subscribe=AutoSubscribe.AUDIO_ONLY)

    # Wait for a participant to connect
    participant = await ctx.wait_for_participant()
    
    # Create the assistant instance
    assistant = await create_assistant(ctx=ctx, initial_ctx=initial_chat_ctx)

    # Start the assistant
    assistant.start(ctx.room, participant)

    # Greet the participant
    await assistant.say("Hello!")

if __name__ == "__main__":
    cli.run_app(create_worker_options(prewarm_fnc=prewarm, entrypoint_fnc=entrypoint))
