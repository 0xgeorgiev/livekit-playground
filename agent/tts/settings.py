"""
Voice settings for the TTS
"""
from agent.config.configuration import ELEVENLABS
from livekit.plugins.elevenlabs import VoiceSettings, Voice

voice_settings = VoiceSettings(
    stability=ELEVENLABS.stability,
    similarity_boost=ELEVENLABS.similarity_boost,
    style=ELEVENLABS.style
)

voice = Voice(
    id=ELEVENLABS.voice_id,
    name=ELEVENLABS.voice_name,
    category=ELEVENLABS.voice_category,
    settings=voice_settings,
)

ELEVENLABS_TTS_SETTINGS = {
    "model": ELEVENLABS.model,
    "voice": voice,
}
