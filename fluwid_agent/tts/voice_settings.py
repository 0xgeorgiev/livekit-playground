"""
Voice settings for the TTS
"""

from livekit.plugins.elevenlabs import VoiceSettings

voice_settings = VoiceSettings(
    stability=0.5,
    similarity_boost=0.75,
    style=0.0
)
