"""
Voice configuration for the TTS
"""
from livekit.plugins.elevenlabs import Voice
from fluwid_agent.configuration import ELEVENLABS
from fluwid_agent.tts.settings import voice_settings

voice = Voice(
    id=ELEVENLABS.voice_id,
    name=ELEVENLABS.voice_name,
    category="premade",
    settings=voice_settings,
)
