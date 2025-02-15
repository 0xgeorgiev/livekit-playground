"""
Implementation of Claude LLM
"""
import os
from dotenv import load_dotenv
from livekit.plugins import anthropic

load_dotenv()

claude_llm = anthropic.LLM(
    model="claude-3-5-sonnet-20241022",
    api_key=os.getenv("ANTHROPIC_API_KEY")
)