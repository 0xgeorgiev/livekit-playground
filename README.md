# Voice Assistant

General voice assistant

## Features

- Real-time voice interaction using LiveKit
- Speech-to-text using Deepgram
- Natural language processing using Claude 3 Sonnet
- Text-to-speech using ElevenLabs with custom voice
- Automated follow-up calls in Bulgarian
- Usage metrics collection

## Prerequisites

- Python 3.12
- Poetry (Python package manager)
- API keys for:
  - LiveKit
  - Anthropic Claude
  - ElevenLabs
  - Deepgram

## Installation

1. Clone the repository:
   ```bash
   git clone [repository-url]
   cd [repository-name]
   ```

2. Install Poetry if you haven't already:
   ```bash
   curl -sSL https://install.python-poetry.org | python3 -
   ```

3. Install dependencies:
   ```bash
   poetry install
   ```

4. Set up environment variables by copying `.env.example` to `.env`:
   ```bash
   cp .env.example .env
   ```

5. Configure the following variables in `.env`:
   ```
   LIVEKIT_SERVER_URL=your_livekit_server_url
   LIVEKIT_API_KEY=your_livekit_api_key
   LIVEKIT_API_SECRET=your_livekit_api_secret
   ANTHROPIC_API_KEY=your_anthropic_api_key
   ELEVEN_LABS_API_KEY=your_elevenlabs_api_key
   ELEVEN_LABS_VOICE_ID=your_elevenlabs_voice_id
   DEEPGRAM_API_KEY=your_deepgram_api_key
   ```

## Usage

1. Create a room in LiveKit (through dashboard or API)

2. Start the voice assistant:
   ```bash
   python main.py start
   python main.py dev --room your-room-name
   ```

3. The assistant will:
   - Connect to the specified room
   - Wait for a participant to join
   - Start the conversation in Bulgarian
   - Process voice input and provide responses
   - Collect usage metrics

## Project Structure

```
livekit_playground/
├── agent/
│   ├── agent.py        # Voice pipeline agent configuration
│   ├── context.py      # Conversation context and prompts
│   └── options.py      # Worker options configuration
├── speech_to_text/
│   └── deepgram.py     # Deepgram STT configuration
├── text_to_speech/
│   └── eleven_labs.py  # ElevenLabs TTS configuration
├── large_language_models/
│   └── anthropic.py    # Claude LLM configuration
└── main.py             # Application entrypoint
```

## Development

```bash
# Format code
poetry run black .

# Sort imports
poetry run isort .

# Lint code
poetry run flake8
```

## Environment Variables

Required environment variables:
- `LIVEKIT_SERVER_URL`: WebSocket URL for LiveKit server
- `LIVEKIT_API_KEY`: LiveKit API key
- `LIVEKIT_API_SECRET`: LiveKit API secret
- `ANTHROPIC_API_KEY`: Anthropic API key for Claude
- `ELEVEN_LABS_API_KEY`: ElevenLabs API key
- `DEEPGRAM_API_KEY`: Deepgram API key
