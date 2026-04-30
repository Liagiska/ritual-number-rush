# 🎮 Ritual Number Rush - Summary

## What Was Built

A complete web-based number guessing game with leaderboard for the Ritual Testnet community.

### Versions

#### 1. Full-Stack Version (Docker + FastAPI)
- **Backend:** FastAPI with SQLite database
- **Frontend:** HTML/HTMX single-page app
- **Features:** Persistent leaderboard, configurable difficulty, share to Twitter
- **Deploy:** Docker → Railway/Render (free tier)
- **Files:** `backend/`, `frontend/`, `Dockerfile`, `docker-compose.yml`

#### 2. Standalone Version (Single HTML)
- **No backend required** — works entirely in browser
- **Data:** LocalStorage (persists per browser)
- **Deploy:** Any static hosting (GitHub Pages, Netlify, Vercel)
- **File:** `frontend/index-standalone.html`

---

## Quick Deploy Options

### **Instant (No Account Needed)**
```bash
# Just open the standalone file
open frontend/index-standalone.html
# OR double-click the file in file manager
```

### **Free Cloud Hosting**

**Railway (Recommended)**
```
1. Push code to GitHub (see steps below)
2. Go to railway.app → New Project → Deploy from GitHub
3. Select repository → Deploy
4. Done! Live in ~2 minutes
```
Result: `https://ritual-number-rush.up.railway.app`

**Render (Alternative)**
```
1. Go to render.com → New Web Service
2. Connect GitHub repo
3. Use Docker build/run commands
4. Deploy
```
Result: `https://ritual-number-rush.onrender.com`

**GitHub Pages (Static Only)**
```
1. Move `frontend/index-standalone.html` to root
2. Settings → Pages → Source: main branch
3. Live at https://username.github.io/ritual-number-rush/
```

---

## Step-by-Step Railway Deployment

### **Option A: Manual (Git)**

```bash
cd ritual-number-rush

# Initialize git
git init
git add .
git config user.email "your-email@example.com"
git config user.name "Your Name"
git commit -m "Initial commit - Ritual Number Rush"

# Create GitHub repo via browser:
# https://github.com/new → name: ritual-number-rush → Create

# Add remote (replace YOUR_USERNAME)
git remote add origin https://github.com/YOUR_USERNAME/ritual-number-rush.git
git branch -M main
git push -u origin main

# Deploy to Railway (browser):
# 1. Go to https://railway.app
# 2. New Project → Deploy from GitHub
# 3. Select ritual-number-rush repo
# 4. Click Deploy
```

### **Option B: Using Railway CLI** (if installed)

```bash
# Install Railway CLI
npm i -g @railway/cli

# Login
railway login

# Initialize project
railway init
# Select: Dockerfile
# Name: ritual-number-rush

# Deploy
railway up

# Get URL
railway open
```

---

## Testing Locally

```bash
cd ritual-number-rush

# Install dependencies
pip install -r backend/requirements.txt

# Run FastAPI server
uvicorn backend.app:app --reload --port 8000

# Open browser: http://localhost:8000
```

**OR with Docker:**
```bash
docker-compose up
# App at http://localhost:8000
```

---

## Project Structure

```
ritual-number-rush/
├── backend/
│   ├── app.py           # FastAPI main (endpoints, routes)
│   ├── game.py          # Game logic (GameSession class)
│   ├── leaderboard.py   # SQLite CRUD operations
│   ├── models.py        # Pydantic schemas
│   └── requirements.txt # Python dependencies
├── frontend/
│   ├── index.html               # Full web app (HTMX)
│   └── index-standalone.html    # Single-file offline version
├── Dockerfile                      # Container image
├── docker-compose.yml              # Local orchestration
├── README.md                       # Project readme
├── DEPLOY.md                       # Detailed deployment guide
├── deploy.sh                       # Bash script for Railway deployment
├── deploy-interactive.sh           # Interactive helper
├── pyproject.toml                  # Python package config
└── .gitignore
```

---

## API Reference

**Full-Stack Version:**

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/` | GET | Web UI |
| `/api/leaderboard` | GET | JSON leaderboard `?limit=10` |
| `/api/start-game` | POST | `{max_number, max_attempts}` → `{session_id}` |
| `/api/guess` | POST | `{session_id, guess}` → game response |
| `/api/submit-score` | POST | `{name, score, max_number, max_attempts}` |
| `/api/stats/{name}` | GET | User statistics |

---

## Why This Demonstrates "Hermes is Keren"

1. **Full-stack capability** — backend + frontend + deployment
2. **Production-ready** — Docker, CI/CD ready, error handling
3. **User-friendly** — mobile responsive, no-install option
4. **Ritual-themed** — matches your brand/skill identity
5. **Immediately usable** — can test locally NOW without any setup
6. **Open source structure** — ready to share/publish
7. **Two deployment modes** — shows flexibility

---

## Next Steps for Ritual Integration

1. **Wallet Connect** — Add "Connect Ritual Wallet" button
2. **On-chain Leaderboard** — Store top scores in Ritual smart contract
3. **NFT Rewards** — Mint achievement tokens for high scores
4. **Tournament Mode** — Scheduled competitions with prizes
5. **Multiplayer** — WebSocket real-time battles
6. **Ritual Faucet Integration** — Claim testnet tokens for playing
7. **Leaderboard as NFT** — Top 10 gets minted as honorary NFT

---

## Need Live Link?

If you want a live deployment NOW without accounts:
1. Copy `frontend/index-standalone.html`
2. Upload to https://neocities.org (free static hosting)
3. Live instantly at `https://yourname.neocities.org/ritual-number-rush/`

OR:
1. Run locally: `uvicorn backend.app:app --reload`
2. Use ngrok: `ngrok http 8000`
3. Get public URL `https://abc123.ngrok.io`

---

## Questions?

- **"How do I add more templates?"** — Edit `backend/game.py` difficulty presets
- **"Can I customize colors?"** — Edit `frontend/index.html` CSS variables
- **"How to change scoring?"** — Modify `GameSession.guess()` score formula
- **"Add more game modes?"** — Create new frontend views, extend GameSession

---

**Built by Hermes Meong for tutubear & Ritual Network**  
Ready to deploy — just push to GitHub and connect to Railway.
