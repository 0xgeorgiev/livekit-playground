"""
Eleven Labs TTS impementation
"""
from livekit.plugins.elevenlabs import Voice, tts
from fluwid_agent.configuration import ELEVENLABS
from fluwid_agent.tts.voice import voice

if not ELEVENLABS.api_key:
    raise ValueError("ELEVENLABS_API_KEY environment variable is not set")

eleven_labs_tts = tts.TTS(
    model="eleven_turbo_v2_5",
    api_key=ELEVENLABS.api_key,
    voice=voice,
)
