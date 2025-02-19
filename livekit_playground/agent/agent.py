"""
Implementation of Agent
"""
from livekit.agents import JobContext, llm
from livekit.agents.pipeline import VoicePipelineAgent
from livekit_playground.speech_to_text.deepgram import deepgram_stt
from livekit_playground.text_to_speech.eleven_labs import eleven_labs_tts
from livekit_playground.large_language_models.anthropic import anthropic_claude_llm

async def create_agent(ctx: JobContext, initial_ctx: llm.ChatContext) -> VoicePipelineAgent:
    """
    Create and return configured voice pipeline agent
    """
    agent = VoicePipelineAgent(
        vad=ctx.proc.userdata["vad"],
        llm=anthropic_claude_llm,
        stt=deepgram_stt,
        tts=eleven_labs_tts,
        chat_ctx=initial_ctx,
    )
    return agent
