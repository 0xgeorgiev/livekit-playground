"""
Settings for the LLM models
"""
from fluwid_agent.configuration.config import ANTHROPIC

ANTHROPIC_LLM_SETTINGS = {
    "model": ANTHROPIC.model,
    "temperature": ANTHROPIC.temperature,
}
