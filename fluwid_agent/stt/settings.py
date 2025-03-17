"""
Settings for Deepgram STT
"""
from fluwid_agent.stt.keywords import KEYWORDS
from fluwid_agent.stt.keyterms import KEYTERMS
from fluwid_agent.configuration.config import DEEPGRAM

DEEPGRAM_STT_SETTINGS = {
    "model": DEEPGRAM.model,
    "language": DEEPGRAM.language,
    "keywords": KEYWORDS,
    "keyterms": KEYTERMS,
}
