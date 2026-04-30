import random
from dataclasses import dataclass
from typing import Optional
import uuid

@dataclass
class GameSession:
    target: int
    attempts: int
    max_attempts: int
    max_number: int
    guesses: list
    session_id: str

    @classmethod
    def create(cls, max_number: int = 100, max_attempts: int = 10) -> 'GameSession':
        return cls(
            target=random.randint(1, max_number),
            attempts=0,
            max_attempts=max_attempts,
            max_number=max_number,
            guesses=[],
            session_id=str(uuid.uuid4())[:8]
        )

    def guess(self, number: int) -> dict:
        self.attempts += 1
        self.guesses.append(number)

        if number == self.target:
            score = max(0, 100 - (self.attempts * 10))
            return {
                "result": "correct",
                "attempts": self.attempts,
                "score": score,
                "game_over": True,
                "message": f"🎉 Correct! The number was {self.target}."
            }
        elif self.attempts >= self.max_attempts:
            return {
                "result": "fail",
                "attempts": self.attempts,
                "score": 0,
                "game_over": True,
                "message": f"💥 Game Over! The number was {self.target}."
            }
        else:
            hint = "higher" if number < self.target else "lower"
            return {
                "result": hint,
                "attempts": self.attempts,
                "score": None,
                "game_over": False,
                "message": f"Try {'📈 higher' if hint == 'higher' else '📉 lower'}!"
            }
