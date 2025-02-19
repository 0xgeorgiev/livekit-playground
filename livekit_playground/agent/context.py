"""
Agent context and configuration
"""
from livekit.agents import llm

def create_initial_context() -> llm.ChatContext:
    """
    Create and return the initial chat context for the agent
    """
    return llm.ChatContext().append(
        role="system",
        text=(
            "You are a voice assistant created by LiveKit. Your interface with users will be voice. "
            "You should use short and concise responses, and avoiding usage of unpronounceable punctuation. "
            "You were created as a demo to showcase the capabilities of LiveKit's agents framework."
        )
    ) 
