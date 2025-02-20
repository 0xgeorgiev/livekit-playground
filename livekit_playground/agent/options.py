"""
Agent worker options
"""
import os
from typing import Callable
from livekit.agents import WorkerOptions
from dotenv import load_dotenv

def create_worker_options(prewarm_fnc: Callable, entrypoint_fnc: Callable) -> WorkerOptions:
    """
    Create and return worker options
    """
    load_dotenv()  # Ensure env vars are loaded
    
    ws_url = os.getenv("LIVEKIT_SERVER_URL")
    api_key = os.getenv("LIVEKIT_API_KEY")
    api_secret = os.getenv("LIVEKIT_API_SECRET")

    if not all([ws_url, api_key, api_secret]):
        raise ValueError("Missing required LiveKit credentials in environment variables")

    return WorkerOptions(
        entrypoint_fnc=entrypoint_fnc,
        prewarm_fnc=prewarm_fnc,
        agent_name="agent-elena",
        ws_url=ws_url,
        api_key=api_key,
        api_secret=api_secret
    )
