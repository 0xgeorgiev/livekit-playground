"""
Deepgram STT implementation
"""
from livekit.plugins import deepgram
from fluwid_agent.stt.keywords import KEYWORDS
from fluwid_agent.stt.keyterms import KEYTERMS
from fluwid_agent.stt.settings import DEEPGRAM_SETTINGS
from fluwid_agent.configuration import DEEPGRAM

if not DEEPGRAM.api_key:
    raise ValueError("DEEPGRAM_API_KEY environment variable is not set")

deepgram_stt = deepgram.STT(
    **DEEPGRAM_SETTINGS,
    keywords=KEYWORDS,
    keyterms=KEYTERMS,
    api_key=DEEPGRAM.api_key,
)
