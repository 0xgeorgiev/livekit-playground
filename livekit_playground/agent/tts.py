"""
Text-to-speach configuration
"""
import os
from dotenv import load_dotenv
from livekit.plugins import elevenlabs
from livekit.plugins.elevenlabs import Voice

load_dotenv()

custom_voice = Voice(
    id="fSxb5mPM1l5zTVVtM3Vb",
    name="Elena",
    category='custom'
)

eleven_tts = elevenlabs.TTS(
    model="eleven_turbo_v2_5",
    api_key=os.getenv("ELEVEN_LABS_API_KEY"),
    voice=custom_voice
)