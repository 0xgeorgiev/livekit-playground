"""
Deepgram speech-to-text configuration
"""
from livekit.plugins import deepgram
from fluwid_agent.configuration import DEEPGRAM
from fluwid_agent.stt.keywords import KEYWORDS
from fluwid_agent.stt.keyterms import KEYTERMS

# Validate Deepgram API key
if not DEEPGRAM.api_key:
    raise ValueError("DEEPGRAM_API_KEY environment variable is not set")

deepgram_stt = deepgram.STT(
    model=DEEPGRAM.model,
    language=DEEPGRAM.language, # type: ignore
    detect_language=DEEPGRAM.detect_language,
    punctuate=DEEPGRAM.punctuate,
    smart_format=DEEPGRAM.smart_format,
    sample_rate=DEEPGRAM.sample_rate,
    no_delay=DEEPGRAM.no_delay,
    endpointing_ms=DEEPGRAM.endpointing_ms,
    filler_words=DEEPGRAM.filler_words,
    interim_results=DEEPGRAM.interim_results,
    keywords=KEYWORDS,
    keyterms=KEYTERMS,
    api_key=DEEPGRAM.api_key,
)
