"""
Deepgram speech-to-text configuration
"""
import os
from dotenv import load_dotenv
from livekit.plugins import deepgram

load_dotenv()

api_key = os.getenv("DEEPGRAM_API_KEY")
if not api_key:
    raise ValueError("DEEPGRAM_API_KEY environment variable is not set")

deepgram_stt = deepgram.STT(
    model="nova-2-phonecall",
    api_key=api_key,
    language="bg" # type: ignore
)
