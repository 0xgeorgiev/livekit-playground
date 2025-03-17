"""
Implementation of Anthropic LLM
"""
from livekit.plugins import anthropic
from fluwid_agent.configuration.config import ANTHROPIC
from fluwid_agent.llm.settings import ANTHROPIC_LLM_SETTINGS

try:
    if not ANTHROPIC.api_key:
        raise ValueError("ANTHROPIC_API_KEY environment variable is not set")

    anthropic_llm = anthropic.LLM(
        api_key=ANTHROPIC.api_key,
        **ANTHROPIC_LLM_SETTINGS
    )

except Exception as ex:
    raise RuntimeError(f"Failed to initialize Anthropic LLM: {str(ex)}") from ex

def get_anthropic_llm() -> anthropic.LLM:
    """
    Get the Anthropic LLM
    """
    return anthropic_llm
