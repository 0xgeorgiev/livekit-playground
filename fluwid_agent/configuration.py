"""
Central configuration module for the Fluwit Agent.

This module centralizes all configuration settings and environment variables
used throughout the application. It loads environment variables from .env file
and provides structured access to configuration settings.
"""
import os
from dataclasses import dataclass
from dotenv import load_dotenv

load_dotenv()

@dataclass
class DeepgramConfig:
    """
    Deepgram STT configuration
    """
    api_key: str = os.getenv("DEEPGRAM_API_KEY", "")


@dataclass
class MongoDBConfig:
    """
    MongoDB connection configuration
    """
    cluster: str = os.getenv("MONGODB_CLUSTER_URI", "mongodb://localhost:27017")
    database: str = os.getenv("MONGODB_DATABASE", "fluwit_agent")
    agent_contexts_collection: str = os.getenv("MONGODB_AGENT_CONTEXTS_COLLECTION", "agent_contexts")


@dataclass
class ElevenLabsConfig:
    """
    ElevenLabs text-to-speech configuration
    """
    api_key: str = os.getenv("ELEVENLABS_API_KEY", "")
    voice_id: str = os.getenv("ELEVENLABS_VOICE_ID", "")
    voice_name: str = os.getenv("ELEVENLABS_VOICE_NAME", "")


@dataclass
class LiveKitConfig:
    """
    LiveKit server configuration
    """
    server_url: str = os.getenv("LIVEKIT_SERVER_URL", "")
    api_key: str = os.getenv("LIVEKIT_API_KEY", "")
    api_secret: str = os.getenv("LIVEKIT_API_SECRET", "")


@dataclass
class AnthropicConfig:
    """
    Anthropic API configuration
    """
    api_key: str = os.getenv("ANTHROPIC_API_KEY", "")
    model: str = os.getenv("ANTHROPIC_MODEL", "claude-3-opus-20240229")


# Create configuration instances
MONGODB = MongoDBConfig()
ELEVENLABS = ElevenLabsConfig()
LIVEKIT = LiveKitConfig()
ANTHROPIC = AnthropicConfig()


# Validate critical configuration
def validate_config():
    """
    Validate that critical configuration values are set.
    Raises ValueError if any required configuration is missing.
    """
    missing_configs = []
    
    # Check MongoDB configuration
    if not MONGODB.cluster:
        missing_configs.append("MONGODB_CLUSTER_URI")
    
    # Check ElevenLabs configuration
    if not ELEVENLABS.api_key:
        missing_configs.append("ELEVENLABS_API_KEY")
    if not ELEVENLABS.voice_id:
        missing_configs.append("ELEVENLABS_VOICE_ID")
    
    # Check LiveKit configuration
    if not LIVEKIT.server_url:
        missing_configs.append("LIVEKIT_SERVER_URL")
    if not LIVEKIT.api_key:
        missing_configs.append("LIVEKIT_API_KEY")
    if not LIVEKIT.api_secret:
        missing_configs.append("LIVEKIT_API_SECRET")
    
    # Check Anthropic configuration
    if not ANTHROPIC.api_key:
        missing_configs.append("ANTHROPIC_API_KEY")
    
    if missing_configs:
        raise ValueError(f"Missing required environment variables: {', '.join(missing_configs)}")


# Optional: Uncomment to validate configuration at import time
# validate_config()
