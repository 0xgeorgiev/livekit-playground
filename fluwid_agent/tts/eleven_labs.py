"""
Eleven Labs text-to-speech configuration
"""
from livekit.plugins.elevenlabs import Voice, tts
from fluwid_agent.configuration import ELEVENLABS
from fluwid_agent.tts.voice_settings import voice_settings

# Validate ElevenLabs API key
if not ELEVENLABS.api_key:
    raise ValueError("ELEVENLABS_API_KEY environment variable is not set")

# Validate ElevenLabs voice ID
if not ELEVENLABS.voice_id:
    raise ValueError("ELEVENLABS_VOICE_ID environment variable is not set")

eleven_labs_tts = tts.TTS(
    model="eleven_turbo_v2_5",
    api_key=ELEVENLABS.api_key,
    voice=Voice(
        id=ELEVENLABS.voice_id,
        name="Elena",
        category="premade",
        settings=voice_settings,
    ),
    # language="bg"
)
