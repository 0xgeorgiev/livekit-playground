"""
Implementation of Claude Sonnet LLM
"""
from livekit.plugins import anthropic
from fluwid_agent.configuration import ANTHROPIC

# Validate Anthropic API key
if not ANTHROPIC.api_key:
    raise ValueError("ANTHROPIC_API_KEY environment variable is not set")

anthropic_claude_llm = anthropic.LLM(
    model=ANTHROPIC.model,
    api_key=ANTHROPIC.api_key
)
