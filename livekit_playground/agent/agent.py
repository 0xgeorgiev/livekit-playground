"""
Implementation of Agent
"""
from livekit.agents import JobProcess, JobContext, llm
from livekit.plugins import silero
from livekit.agents.pipeline import VoicePipelineAgent
from livekit_playground.agent.llm import claude_llm
from livekit_playground.agent.stt import deepgram_transcriber
from livekit_playground.agent.tts import eleven_tts

def prewarm(proc: JobProcess):
    """
    Initialize and load VAD model before processing
    """
    proc.userdata["vad"] = silero.VAD.load()

async def create_agent(ctx: JobContext, initial_ctx: llm.ChatContext) -> VoicePipelineAgent:
    """
    Create and return configured voice pipeline agent
    """
    agent = VoicePipelineAgent(
        vad=ctx.proc.userdata["vad"],
        llm=claude_llm,
        stt=deepgram_transcriber,
        tts=eleven_tts,
        chat_ctx=initial_ctx,
        min_endpointing_delay=0.5,
        max_endpointing_delay=5.0
    )
    return agent
