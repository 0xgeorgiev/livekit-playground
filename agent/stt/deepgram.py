"""
Deepgram STT implementation
"""
from livekit.plugins import deepgram
from agent.configuration.config import DEEPGRAM
from agent.stt.settings import DEEPGRAM_STT_SETTINGS

if not DEEPGRAM.api_key:
    raise ValueError("DEEPGRAM_API_KEY environment variable is not set")

deepgram_stt = deepgram.STT(
    api_key=DEEPGRAM.api_key,
    **DEEPGRAM_STT_SETTINGS,
)

def get_deepgram_stt() -> deepgram.STT:
    """
    Get Deepgram STT
    """
    return deepgram_stt
