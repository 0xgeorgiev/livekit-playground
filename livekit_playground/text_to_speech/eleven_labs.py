"""
Eleven Labs text-to-speech configuration
"""
import os
from dotenv import load_dotenv
from livekit.plugins import elevenlabs
from livekit.plugins.elevenlabs import Voice

load_dotenv()

api_key = os.getenv("ELEVEN_LABS_API_KEY")
if not api_key:
    raise ValueError("ELEVEN_LABS_API_KEY environment variable is not set")

voice_id = os.getenv("ELEVEN_LABS_VOICE_ID")
if not voice_id:
    raise ValueError("ELEVEN_LABS_VOICE_ID environment variable is not set")

# TODO: double check if this is correct
custom_voice = Voice(
    id=voice_id,
    name="Elena",
    category='custom'
)

eleven_labs_tts = elevenlabs.TTS(
    model="eleven_turbo_v2_5",
    api_key=api_key,
    voice=custom_voice
)
