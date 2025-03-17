"""
Assistant settings
"""
from fluwid_agent.configuration.config import ASSISTANT

ASSISTANT_SETTINGS = {
    #"before_llm_cb": ASSISTANT.before_llm_cb,
    #"before_tts_cb": ASSISTANT.before_tts_cb,
    # "fnc_context": ASSISTANT.fnc_context,
    "allow_interruptions": ASSISTANT.allow_interruptions,
    "turn_detector": ASSISTANT.turn_detector,
}
