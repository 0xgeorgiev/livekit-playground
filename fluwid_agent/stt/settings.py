"""
Deepgram STT settings
"""

DEEPGRAM_SETTINGS = {
    "model": "nova-2-general",
    "language": "bg",
    "detect_language": False,
    "punctuate": True,
    "smart_format": True,
    "sample_rate": 16000,
    "no_delay": True,
    "endpointing_ms": 25,
    "filler_words": True,
    "interim_results": True,
}
