"""
Worker options
"""
from typing import Callable
from livekit.agents import WorkerOptions, WorkerType
from fluwid_agent.configuration.config import LIVEKIT, AGENT

def get_worker_options(prewarm_fnc: Callable, entrypoint_fnc: Callable) -> WorkerOptions:
    """
    Create and return worker options
    """
    if not all([LIVEKIT.server_url, LIVEKIT.api_key, LIVEKIT.api_secret]):
        raise ValueError("Missing required LiveKit credentials in environment variables")

    return WorkerOptions(
        entrypoint_fnc=entrypoint_fnc,
        prewarm_fnc=prewarm_fnc,
        agent_name=AGENT.name,
        ws_url=LIVEKIT.server_url,
        api_key=LIVEKIT.api_key,
        api_secret=LIVEKIT.api_secret,
        worker_type=WorkerType.ROOM
    )
