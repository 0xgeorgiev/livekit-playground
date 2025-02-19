"""
Implementation of Claude Sonnet LLM
"""
import os
from dotenv import load_dotenv
from livekit.plugins import anthropic

load_dotenv()

api_key = os.getenv("ANTHROPIC_API_KEY")
if not api_key:
    raise ValueError("ANTHROPIC_API_KEY environment variable is not set")

anthropic_claude_llm = anthropic.LLM(
    model="claude-3-5-sonnet-20241022",
    api_key=api_key
)
