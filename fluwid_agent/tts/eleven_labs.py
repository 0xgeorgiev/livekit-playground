"""
Eleven Labs TTS impementation
"""
from livekit.plugins.elevenlabs import tts
from fluwid_agent.configuration.config import ELEVENLABS
from fluwid_agent.tts.settings import ELEVENLABS_TTS_SETTINGS

if not ELEVENLABS.api_key:
    raise ValueError("ELEVENLABS_API_KEY environment variable is not set")

eleven_labs_tts = tts.TTS(
    api_key=ELEVENLABS.api_key,
    **ELEVENLABS_TTS_SETTINGS,
)

def get_eleven_labs_tts() -> tts.TTS:
    """
    Get Eleven Labs TTS
    """
    return eleven_labs_tts
