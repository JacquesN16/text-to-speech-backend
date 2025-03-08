from TTS.api import TTS
import io
import logging
from typing import Optional

logger = logging.getLogger(__name__)

class TTSManager:
    _instance: Optional[TTS] = None

    @classmethod
    def get_instance(cls, model_name: str) -> TTS:
        if cls._instance is None:
            try:
                logger.info(f"Initializing TTS with model: {model_name}")
                cls._instance = TTS(model_name=model_name, progress_bar=False)
                logger.info("TTS initialization successful")
            except Exception as e:
                logger.error(f"Failed to initialize TTS: {str(e)}")
                raise
        return cls._instance

    @classmethod
    def generate_speech(cls, text: str, model_name: str) -> io.BytesIO:
        tts = cls.get_instance(model_name)
        
        # Generate speech
        wav = tts.tts(text)
        
        # Create an in-memory bytes buffer
        wav_bytes = io.BytesIO()
        tts.synthesizer.save_wav(wav, wav_bytes)
        wav_bytes.seek(0)
        
        return wav_bytes
