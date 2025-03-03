"""
Eleven Labs text-to-speech configuration
"""
import os
from dotenv import load_dotenv
from livekit.plugins.elevenlabs import Voice, VoiceSettings, tts

load_dotenv()

api_key = os.getenv("ELEVENLABS_API_KEY")
if not api_key:
    raise ValueError("ELEVENLABS_API_KEY environment variable is not set")

voice_id = os.getenv("ELEVENLABS_VOICE_ID")
if not voice_id:
    raise ValueError("ELEVENLABS_VOICE_ID environment variable is not set")

eleven_labs_tts = tts.TTS(
    model="eleven_turbo_v2_5",
    api_key=api_key,
    voice=Voice(
        id=voice_id,
        name="Elena",
        category="premade",
        settings=VoiceSettings(stability=0.5, similarity_boost=0.75, style=0.0),
    ),
)
