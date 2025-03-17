"""
Implementation of Voice Pipeline Agent
"""
from livekit.agents import JobContext, llm
from livekit.agents.pipeline import VoicePipelineAgent
from fluwid_agent.stt.deepgram import get_deepgram_stt
from fluwid_agent.tts.eleven_labs import get_eleven_labs_tts
from fluwid_agent.llm.anthropic_llm import get_anthropic_llm
from fluwid_agent.assistant.settings import ASSISTANT_SETTINGS

async def create_assistant(ctx: JobContext, initial_ctx: llm.ChatContext) -> VoicePipelineAgent:
    """
    Create and return preconfigured Voice Pipeline Agent
    """
    try:
        assistant = VoicePipelineAgent(
            vad=ctx.proc.userdata["vad"],
            llm=get_anthropic_llm(),
            stt=get_deepgram_stt(),
            tts=get_eleven_labs_tts(),
            chat_ctx=initial_ctx,
            **ASSISTANT_SETTINGS
        )
        return assistant

    except ValueError as ex:
        raise ValueError(f"Failed to create voice pipeline agent - invalid configuration: {str(ex)}")
    
    except Exception as ex:
        raise RuntimeError(f"Failed to create voice pipeline agent: {str(ex)}") from ex
