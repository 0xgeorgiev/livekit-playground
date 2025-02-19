"""
Agent worker options
"""
from typing import Callable
from livekit.agents import WorkerOptions

def create_worker_options(prewarm_fnc: Callable, entrypoint_fnc: Callable) -> WorkerOptions:
    """
    Create and return worker options
    """
    return WorkerOptions(
        entrypoint_fnc=entrypoint_fnc,
        prewarm_fnc=prewarm_fnc,
        agent_name="outbound-agent",
    )