"""
Settings for Deepgram STT
"""
from agent.stt.keywords import KEYWORDS
from agent.stt.keyterms import KEYTERMS
from agent.configuration.config import DEEPGRAM

DEEPGRAM_STT_SETTINGS = {
    "model": DEEPGRAM.model,
    "language": DEEPGRAM.language,
    "keywords": KEYWORDS,
    "keyterms": KEYTERMS,
}
