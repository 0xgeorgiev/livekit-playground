"""
Speach-to-text configuration
"""
import os
from dotenv import load_dotenv
from livekit.plugins import deepgram

load_dotenv()

deepgram_transcriber = deepgram.STT(
    model="nova-2-general",
    api_key=os.getenv("DEEPGRAM_API_KEY"),
    language="bg" # type: ignore
)