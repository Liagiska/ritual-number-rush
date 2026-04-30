from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from contextlib import asynccontextmanager
import uvicorn

from game import GameSession
from leaderboard import add_score, get_leaderboard, get_user_stats, init_db

# In-memory game sessions (production: Redis)
active_games = {}

@asynccontextmanager
async def lifespan(app: FastAPI):
    init_db()
    yield

app = FastAPI(title="Ritual Number Rush", lifespan=lifespan)

# API Routes

@app.get("/api/leaderboard")
async def api_leaderboard(limit: int = 10):
    entries = get_leaderboard(limit)
    for i, entry in enumerate(entries):
        entry["rank"] = i + 1
    return {"success": True, "data": entries}

@app.post("/api/start-game")
async def start_game(config: dict):
    max_number = config.get("max_number", 100)
    max_attempts = config.get("max_attempts", 10)
    session = GameSession.create(max_number, max_attempts)
    active_games[session.session_id] = session
    return {
        "success": True,
        "session_id": session.session_id,
        "max_number": session.max_number,
        "max_attempts": session.max_attempts,
        "attempts_remaining": session.max_attempts
    }

@app.post("/api/guess")
async def make_guess(request: dict):
    session_id = request.get("session_id")
    guess = request.get("guess")

    if not session_id or session_id not in active_games:
        raise HTTPException(status_code=400, detail="Invalid or expired session")

    session = active_games[session_id]
    result = session.guess(guess)

    response = {
        "success": True,
        "result": result["result"],
        "attempts": result["attempts"],
        "game_over": result["game_over"],
        "message": result["message"],
        "session_id": session_id
    }

    if result["game_over"]:
        response["score"] = result["score"]
        response["target"] = session.target
        del active_games[session_id]

    return response

@app.post("/api/submit-score")
async def submit_score(request: dict):
    name = request.get("name", "").strip()
    score = request.get("score", 0)
    max_number = request.get("max_number", 100)
    max_attempts = request.get("max_attempts", 10)

    if not name:
        raise HTTPException(status_code=400, detail="Name required")

    add_score(name, score, max_number, max_attempts)
    return {"success": True, "message": "Score submitted!"}

@app.get("/api/stats/{name}")
async def get_stats(name: str):
    stats = get_user_stats(name)
    if not stats:
        return {"success": False, "message": "No stats found"}
    return {"success": True, "data": stats}

# Web UI Route

@app.get("/", response_class=HTMLResponse)
async def web_ui(request: Request):
    with open("frontend/index.html", "r") as f:
        html = f.read()
    return HTMLResponse(content=html)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
