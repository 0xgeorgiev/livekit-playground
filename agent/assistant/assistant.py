"""
Implementation of Assistant
"""
from livekit.agents import JobContext, llm
from livekit.agents.pipeline import VoicePipelineAgent
from fluwit_agent.stt.deepgram import deepgram_stt
from fluwit_agent.tts.eleven_labs import eleven_labs_tts
from fluwit_agent.llm.anthropic import anthropic_claude_llm
from fluwit_agent.tools.tools import AssistantTool
async def create_assistant(ctx: JobContext, initial_ctx: llm.ChatContext) -> VoicePipelineAgent:
    """
    Create and return preconfigured Voice Pipeline Agent
    """
    assistant = VoicePipelineAgent(
        vad=ctx.proc.userdata["vad"],
        llm=anthropic_claude_llm,
        stt=deepgram_stt,
        tts=eleven_labs_tts,
        chat_ctx=initial_ctx,
        fnc_ctx=AssistantTool()
    )
    return assistant
