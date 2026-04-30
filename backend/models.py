from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional

class GameConfig(BaseModel):
    max_number: int = Field(100, ge=10, le=1000)
    max_attempts: int = Field(10, ge=5, le=20)

class GuessRequest(BaseModel):
    guess: int = Field(..., ge=1)

class GuessResponse(BaseModel):
    result: str
    attempts: int
    score: Optional[int] = None
    game_over: bool
    message: Optional[str] = None

class LeaderboardEntry(BaseModel):
    rank: int
    name: str
    score: int
    max_number: int
    max_attempts: int
    date: str
    total_games: Optional[int] = None
    win_rate: Optional[float] = None
