"""
Text-to-speach configuration
"""
import os
from dotenv import load_dotenv
from livekit.plugins import elevenlabs

load_dotenv()

eleven_tts = elevenlabs.TTS(
    model="eleven_turbo_v2_5",
    api_key=os.getenv("ELEVEN_LABS_API_KEY"),
)