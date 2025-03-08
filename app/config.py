from pydantic import BaseModel
from functools import lru_cache
from typing import List

class Settings(BaseModel):
    APP_NAME: str = "TTS Backend"
    DEBUG_MODE: bool = False
    MODEL_NAME: str = "tts_models/en/ljspeech/tacotron2-DDC"
    MODEL_PATH: str = "./models"
    MAX_TEXT_LENGTH: int = 1000
    ALLOWED_ORIGINS: list = ["http://localhost:3000"]

    class Config:
        env_file = ".env"

@lru_cache()
def get_settings():
    return Settings()
