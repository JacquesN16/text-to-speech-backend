from fastapi import APIRouter, HTTPException, Depends, Request
from fastapi.responses import StreamingResponse,JSONResponse
from ..core.tts_manager import TTSManager
from .models import TTSRequest, ErrorResponse
from ..config import get_settings
import logging

logger = logging.getLogger(__name__)
router = APIRouter()

@router.get("/ping")
async def ping():
    """
    Health check endpoint to verify the API is running.
    Returns a simple JSON response with status and timestamp.
    """
    from datetime import datetime

    return {
        "status": "ok",
        "message": "TTS Backend API is running",
        "timestamp": datetime.now().isoformat()
    }


@router.post("/tts")
async def text_to_speech(request: Request):
    try:
       json_data = await request.json()
       text = json_data.get("text","")
       print(text)

       if not text:
          raise HTTPException(status_code=400, detail="Text is required")
       wav_bytes = TTSManager.generate_speech(text,"tts_models/en/ljspeech/tacotron2-DDC")

       return StreamingResponse(
            wav_bytes,
            media_type="audio/wav",
            headers={
                "Content-Disposition": "attachment; filename=speech.wav"
            }
        )
    except Exception as e:
        logger.error(f"Error in text_to_speech: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))
