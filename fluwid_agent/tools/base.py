"""
Base tool implementation for the assistant
"""
from livekit.agents import llm

class BaseTool(llm.FunctionContext):
    """
    Base class for all assistant tools
    
    All tools should inherit from this class and implement
    their specific functionality.
    """
    def __init__(self) -> None:
        super().__init__() 
