# LiveKit Playground

A Python project for experimenting with LiveKit.

## Setup

1. Make sure you have Python 3.12 installed
2. Install dependencies:
   ```bash
   poetry install
   ```
3. Copy `.env.example` to `.env` and fill in your LiveKit credentials
4. Run the project:
   ```bash
   poetry run python livekit_playground/main.py
   ```

## Development

- Format code: `poetry run black .`
- Sort imports: `poetry run isort .`
- Lint code: `poetry run flake8`
