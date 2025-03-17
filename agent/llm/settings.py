"""
Settings for the LLM models
"""
from agent.configuration.config import ANTHROPIC

ANTHROPIC_LLM_SETTINGS = {
    "model": ANTHROPIC.model,
    "temperature": ANTHROPIC.temperature,
    "max_tokens": ANTHROPIC.max_tokens,	
}
