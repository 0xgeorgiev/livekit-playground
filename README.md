# Voice Assistant

A general-purpose voice assistant built with LiveKit's agent framework.

## Features

- Real-time voice interaction using LiveKit
- Speech-to-text using Deepgram
- Natural language processing using Claude 3 Sonnet
- Text-to-speech using ElevenLabs with custom voice
- Usage metrics collection

## Prerequisites

- Python 3.12
- Poetry
- API keys for LiveKit, Anthropic Claude, ElevenLabs, and Deepgram

## Quick Start

1. Install dependencies:
   ```bash
   poetry install
   ```

2. Configure environment variables:
   ```bash
   cp .env.example .env
   ```

## Usage

The assistant can be run in different modes:

```bash
# Start in production mode
python main.py start

# Start in development mode with hot reload
python main.py dev --room your-room-name

# Connect to a specific room
python main.py connect your-room-name

# Download required model files
python main.py download-files
```

## Development

```bash
poetry run black .   # Format code
poetry run isort .   # Sort imports
poetry run flake8    # Lint code
```
