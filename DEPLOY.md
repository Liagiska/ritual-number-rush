# Ritual Number Rush - Deployment Guide

## Quick Deploy (3 minutes)

### Option 1: Railway (Recommended - Free Tier)

**Prerequisites:**
- GitHub account
- Railway account (free)

**Steps:**

1. **Manual GitHub Repository Creation**
   - Go to https://github.com/new
   - Repository name: `ritual-number-rush`
   - Set to Public
   - Don't initialize with README
   - Click "Create repository"

2. **Push Code Locally**
   ```bash
   cd ritual-number-rush
   git init
   git add .
   git config user.email "your-email@example.com"
   git config user.name "Your Name"
   git commit -m "Initial commit"
   git branch -M main
   git remote add origin https://github.com/yourusername/ritual-number-rush.git
   git push -u origin main
   ```

3. **Deploy on Railway**
   - Go to https://railway.app
   - Click "New Project"
   - Select "Deploy from GitHub repo"
   - Choose `ritual-number-rush`
   - Railway auto-detects Dockerfile
   - Click "Deploy"

4. **Done!** Your app is live at `https://ritual-number-rush.up.railway.app`

---

### Option 2: Render (Also Free)

1. Go to https://render.com
2. New → Web Service
3. Connect GitHub repo
4. Settings:
   - Name: `ritual-number-rush`
   - Region: Choose nearest
   - Branch: main
   - Build Command: `docker build -t ritual-game .`
   - Start Command: `docker run -p 8000:8000 ritual-game`
5. Create Web Service
6. Wait ~5 min for deployment

---

### Option 3: Docker Local (For Testing)

```bash
cd ritual-number-rush
docker-compose up
# App runs at http://localhost:8000
```

---

## Testing Locally

```bash
cd ritual-number-rush

# Create virtualenv
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r backend/requirements.txt

# Run server
uvicorn backend.app:app --reload --port 8000

# Open browser: http://localhost:8000
```

---

## Features Checklist

- ✅ Number guessing game (1-100)
- ✅ Configurable difficulty (max number, max attempts)
- ✅ Persistent leaderboard (SQLite)
- ✅ Score calculation (100 - attempts*10)
- ✅ Responsive mobile-friendly UI
- ✅ Dark Ritual-themed design
- ✅ Share to Twitter
- ✅ REST API for extensibility

---

## Customization

### Change Theme Colors
Edit `frontend/index.html`: replace `#6366f1` (indigo) and `#8b5cf6` (purple) with your colors.

### Add Game Modes
Modify `backend/game.py` — add difficulty presets (Easy: 1-50, Hard: 1-1000).

### Add Multiplayer
Add WebSocket endpoint in `backend/app.py`, store sessions in Redis instead of dict.

---

## Troubleshooting

**Database errors:**
- Make sure `/app/data` directory is writable (Docker volume)
- Check `data/leaderboard.db` exists

**Port already in use:**
- Change `8000` to another port in `app.py` and Dockerfile

**Leaderboard not updating:**
- Clear `data/leaderboard.db` and restart

---

## Next Steps

1. **Add wallet connection** — integrate with Ritual wallet for on-chain score records
2. **NFT rewards** — mint achievement badges for high scores
3. **Tournaments** — scheduled competitions with prizes
4. **Multiplayer** — real-time head-to-head matches

---

**Built with ❤️ by Hermes & tutubear for Ritual Network**
