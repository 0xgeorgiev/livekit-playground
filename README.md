# LiveKit Voice Assistant

A Python project implementing a voice assistant using LiveKit, Claude, ElevenLabs, and Deepgram.

## Prerequisites

- Python 3.12
- Poetry (Python package manager)
- LiveKit account and credentials
- API keys for:
  - Anthropic Claude
  - ElevenLabs
  - Deepgram

## Setup

1. Make sure you have Python 3.12 installed
2. Install Poetry if you haven't already:
   ```bash
   curl -sSL https://install.python-poetry.org | python3 -
   ```
3. Install dependencies:
   ```bash
   poetry install
   ```
4. Copy `.env.example` to `.env` and fill in your credentials:
   - LIVEKIT_SERVER_URL
   - LIVEKIT_API_KEY
   - LIVEKIT_API_SECRET
   - ANTHROPIC_API_KEY
   - ELEVEN_LABS_API_KEY
   - DEEPGRAM_API_KEY

5. Run the voice assistant:
   ```bash
   poetry run python livekit_playground/main.py
   ```

## Features

- Real-time voice interaction using LiveKit
- Speech-to-text using Deepgram
- Natural language processing using Claude 3 Sonnet
- Text-to-speech using ElevenLabs
- Support for both voice and text chat interactions

## Development

### Code Quality

```bash
# Format code
poetry run black .

# Sort imports
poetry run isort .

# Lint code
poetry run flake8
```

### Project Structure

- `main.py` - Application entrypoint and room management
- `agent/` - Core agent implementation
  - `agent.py` - Voice pipeline agent configuration
  - `llm.py` - Claude LLM integration
  - `stt.py` - Deepgram speech-to-text configuration
  - `tts.py` - ElevenLabs text-to-speech configuration

## Environment Variables

Create a `.env` file with the following variables:

```
LIVEKIT_SERVER_URL=your_livekit_server_url
LIVEKIT_API_KEY=your_livekit_api_key
LIVEKIT_API_SECRET=your_livekit_api_secret
ANTHROPIC_API_KEY=your_anthropic_api_key
ELEVEN_LABS_API_KEY=your_elevenlabs_api_key
DEEPGRAM_API_KEY=your_deepgram_api_key
```
