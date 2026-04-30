# Ritual Number Rush

A simple CLI/web guessing game built for Ritual Testnet community.

## Quick Start (Local)

```bash
git clone <repo>
cd ritual-number-rush
pip install -r backend/requirements.txt
uvicorn backend.app:app --reload
```

Open http://localhost:8000

## Deploy to Railway (1-click)

1. Push to GitHub
2. New Project on Railway
3. Connect repo → Auto-deploy
4. Done! (Free tier included)

## Features

- 🎮 Simple number guessing game
- 🏆 Persistent leaderboard
- 📱 Mobile-friendly
- 🚀 Deploy in minutes
- 💜 Ritual-themed design

## API Endpoints

- `GET /` - Web UI
- `GET /api/leaderboard` - JSON leaderboard
- `POST /api/start-game` - Start new game
- `POST /api/guess` - Submit guess
- `POST /api/submit-score` - Save score

Made with ❤️ by Hermes & tutubear for Ritual Network.
