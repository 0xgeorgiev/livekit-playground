"""
Settings for the LLM models
"""
from agent.configuration import ANTHROPIC_LLM

ANTHROPIC_LLM_SETTINGS = {
    "model": ANTHROPIC_LLM.model,
    "temperature": ANTHROPIC_LLM.temperature,
    "max_tokens": ANTHROPIC_LLM.max_tokens,	
}
