import sqlite3
import json
from datetime import datetime
from pathlib import Path
from typing import List, Optional
from contextlib import contextmanager

DB_PATH = Path("data/leaderboard.db")

@contextmanager
def get_db():
    DB_PATH.parent.mkdir(exist_ok=True)
    conn = sqlite3.connect(str(DB_PATH))
    conn.row_factory = sqlite3.Row
    try:
        yield conn
    finally:
        conn.close()

def init_db():
    with get_db() as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS scores (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                score INTEGER NOT NULL,
                max_number INTEGER NOT NULL,
                max_attempts INTEGER NOT NULL,
                date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)
        conn.execute("""
            CREATE TABLE IF NOT EXISTS stats (
                name TEXT PRIMARY KEY,
                total_games INTEGER DEFAULT 0,
                total_wins INTEGER DEFAULT 0,
                best_score INTEGER DEFAULT 0
            )
        """)
        conn.commit()

def add_score(name: str, score: int, max_number: int, max_attempts: int) -> int:
    with get_db() as conn:
        cur = conn.execute(
            "INSERT INTO scores (name, score, max_number, max_attempts, date) VALUES (?, ?, ?, ?, ?)",
            (name, score, max_number, max_attempts, datetime.now())
        )
        conn.execute("""
            INSERT INTO stats (name, total_games, total_wins, best_score)
            VALUES (?, 1, CASE WHEN ? > 0 THEN 1 ELSE 0 END, ?)
            ON CONFLICT(name) DO UPDATE SET
                total_games = total_games + 1,
                total_wins = total_wins + CASE WHEN ? > 0 THEN 1 ELSE 0 END,
                best_score = MAX(best_score, ?)
        """, (name, score, score, score, score))
        conn.commit()
        return cur.lastrowid

def get_leaderboard(limit: int = 10) -> List[dict]:
    with get_db() as conn:
        rows = conn.execute("""
            SELECT s.*, st.total_games,
                   ROUND(CAST(st.total_wins AS FLOAT) / st.total_games * 100, 2) as win_rate
            FROM scores s
            LEFT JOIN (
                SELECT name, total_games, total_wins FROM stats
            ) st ON s.name = st.name
            ORDER BY s.score DESC, s.date ASC
            LIMIT ?
        """, (limit,)).fetchall()
        return [dict(row) for row in rows]

def get_user_stats(name: str) -> Optional[dict]:
    with get_db() as conn:
        row = conn.execute(
            "SELECT * FROM stats WHERE name = ?",
            (name,)
        ).fetchone()
        return dict(row) if row else None
