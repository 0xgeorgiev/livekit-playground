"""
Assistant settings
"""
from agent.configuration.config import ASSISTANT

ASSISTANT_SETTINGS = {
    "before_llm_cb": ASSISTANT.before_llm_cb,
    "before_tts_cb": ASSISTANT.before_tts_cb,
    "allow_interruptions": ASSISTANT.allow_interruptions,
    "fnc_context": ASSISTANT.fnc_context,
    "turn_detector": ASSISTANT.turn_detector,
}
