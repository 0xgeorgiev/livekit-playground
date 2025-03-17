"""
Central configuration module for the Agent.

This module centralizes all configuration settings and environment variables
used throughout the application. It loads environment variables from .env file
and provides structured access to configuration settings.
"""
import os
from dotenv import load_dotenv
from dataclasses import dataclass
from typing import Optional, Callable

load_dotenv()

@dataclass
class LiveKitConfiguration:
    """
    LiveKit Server configuration
    """
    server_url: str = os.getenv("LIVEKIT_SERVER_URL", "")
    api_key: str = os.getenv("LIVEKIT_API_KEY", "")
    api_secret: str = os.getenv("LIVEKIT_API_SECRET", "")

@dataclass
class DeepgramSTTConfiguration:
    """
    Deepgram STT configuration
    """
    api_key: str = os.getenv("DEEPGRAM_API_KEY", "")
    model: str = os.getenv("DEEPGRAM_MODEL", "nova-2-general")
    language: str = os.getenv("DEEPGRAM_LANGUAGE", "bg")

@dataclass
class AnthropicLLMConfiguration:
    """
    Anthropic API configuration
    """
    api_key: str = os.getenv("ANTHROPIC_API_KEY", "")
    model: str = os.getenv("ANTHROPIC_MODEL", "claude-3-opus-20240229")
    temperature: float = os.getenv("ANTHROPIC_TEMPERATURE", 0.7)
    max_tokens: int = os.getenv("ANTHROPIC_MAX_TOKENS", 250)

@dataclass
class ElevenLabsTTSConfiguration:
    """
    ElevenLabs TTS configuration
    """
    api_key: str = os.getenv("ELEVENLABS_API_KEY", "")
    model: str = os.getenv("ELEVENLABS_MODEL", "eleven_turbo_v2_5")
    voice_id: str = os.getenv("ELEVENLABS_VOICE_ID", "")
    voice_name: str = os.getenv("ELEVENLABS_VOICE_NAME", "Elena")
    voice_category: str = os.getenv("ELEVENLABS_VOICE_CATEGORY", "premade")
    stability: float = os.getenv("ELEVENLABS_STABILITY", 0.5)
    similarity_boost: float = os.getenv("ELEVENLABS_SIMILARITY_BOOST", 0.75)
    style: float = os.getenv("ELEVENLABS_STYLE", 0.0)

@dataclass
class AssistantConfiguration:
    """
    Assistant configuration
    """
    before_llm_cb: Optional[Callable] = None
    before_tts_cb: Optional[Callable] = None
    allow_interruptions: bool = True
    fnc_context: Optional[Callable] = None
    turn_detector: Optional[Callable] = None


LIVEKIT = LiveKitConfiguration()
DEEPGRAM = DeepgramSTTConfiguration()
ANTHROPIC = AnthropicLLMConfiguration()
ELEVENLABS = ElevenLabsTTSConfiguration()
ASSISTANT = AssistantConfiguration()
