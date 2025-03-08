from pydantic import BaseModel, Field
from typing import Optional

class TTSRequest(BaseModel):
    text: str = Field(..., min_length=1, max_length=1000)
    language: Optional[str] = Field(default="en")
    speed: Optional[float] = Field(default=1.0, ge=0.5, le=2.0)

class ErrorResponse(BaseModel):
    detail: str
    error_code: Optional[str] = None
