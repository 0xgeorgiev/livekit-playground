"""
Settings for Deepgram STT
"""
from agent.stt.keywords import KEYWORDS
from agent.stt.keyterms import KEYTERMS
from agent.config.configuration import DEEPGRAM

DEEPGRAM_STT_SETTINGS = {
    "model": DEEPGRAM.model,
    "language": DEEPGRAM.language,
    "keywords": KEYWORDS,
    "keyterms": KEYTERMS,
}
