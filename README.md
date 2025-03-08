# TTS Backend

A FastAPI-based backend service for text-to-speech conversion using the TTS library.

## Features

- Convert text to speech using Tacotron2-DDC model
- Streaming audio response
- Configurable settings via environment variables
- CORS support for frontend integration

## Requirements

- Python 3.8+
- FastAPI
- TTS library
- Other dependencies in requirements.txt

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/tts-backend.git
   cd tts-backend
   ```

2. Create a virtual environment:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

4. Configure environment variables by creating a `.env` file (or edit the existing one):
   ```
   APP_NAME=TTS Backend
   DEBUG_MODE=False
   MODEL_NAME=tts_models/en/ljspeech/tacotron2-DDC
   MODEL_PATH=./models
   MAX_TEXT_LENGTH=1000
   ALLOWED_ORIGINS=["http://localhost:3000"]
   ```

## Usage

1. Start the server:
   ```
   uvicorn app.main:app --reload
   ```

2. Access the API at `http://localhost:8000`

3. Make a POST request to `/api/tts` with JSON data:
   ```json
   {
     "text": "Text to convert to speech"
   }
   ```

4. The response will be an audio file in WAV format.

## API Endpoints

### POST /api/tts

Converts text to speech.

**Request Body:**
```json
{
  "text": "Text to convert to speech"
}
```

**Response:**
- Audio file (WAV format)
- Content-Type: audio/wav

## Configuration

The application can be configured through environment variables in the `.env` file:

- `APP_NAME`: Name of the application
- `DEBUG_MODE`: Enable/disable debug mode
- `MODEL_NAME`: TTS model to use
- `MODEL_PATH`: Path to store models
- `MAX_TEXT_LENGTH`: Maximum allowed text length
- `ALLOWED_ORIGINS`: List of allowed origins for CORS

## License

[MIT License](LICENSE)
