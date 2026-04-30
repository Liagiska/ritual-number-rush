# 🚀 RITUAL NUMBER RUSH — DEPLOYMENT CHEATSHEET

## ✅ PROJECT STATUS: READY TO DEPLOY

**Location:** `/tmp/hermes_sandbox_1z0b2pii/ritual-number-rush/`
**Status:** Backend tested ✓ | Frontend ready ✓ | Docker config ✓

---

## ⚡ INSTANT OPTION (0 setup, 1 minute)

**Deploy the standalone HTML version right now:**

```bash
# Just open this file in any browser:
open /tmp/hermes_sandbox_1z0b2pii/ritual-number-rush/frontend/index-standalone.html
```

**OR** upload `frontend/index-standalone.html` to:
- Neocities (free): https://neocities.org
- GitHub Gist + raw link
- Any static hosting

**Result:** Live URL in <60 seconds, no accounts needed.

---

## 🎯 RECOMMENDED: Railway Deployment (5 minutes)

This gets you the **full-stack version** (FastAPI backend + SQLite database).

### Prerequisites
- GitHub account (free)
- Railway account (free)

### Step-by-Step

**1. Create GitHub Repository**
```bash
cd /tmp/hermes_sandbox_1z0b2pii/ritual-number-rush

git init
git add .
git config user.email "your-email@example.com"
git config user.name "Your Name"
git commit -m "Initial commit - Ritual Number Rush"

# Go to https://github.com/new
# Name: ritual-number-rush
# Set to Public, DON'T initialize with README
# Click "Create repository"

# Copy the repo URL (e.g., https://github.com/username/ritual-number-rush.git)
git remote add origin https://github.com/YOUR_USERNAME/ritual-number-rush.git
git branch -M main
git push -u origin main
```

**2. Deploy to Railway**
```
1. Go to https://railway.app
2. Click "New Project"
3. Click "Deploy from GitHub"
4. Connect GitHub if first time
5. Select repository: ritual-number-rush
6. Railway auto-detects Dockerfile
7. Click "Deploy"
```

**3. Wait ~2 minutes**

**4. Done!**
Your live URL: `https://ritual-number-rush.up.railway.app`

**5. Optional: Set custom domain**
- Settings → Domains → Add domain
- Update DNS (if you own domain)

---

## 🐳 LOCAL TESTING (Before Deploy)

```bash
cd /tmp/hermes_sandbox_1z0b2pii/ritual-number-rush

# Install dependencies
pip install -r backend/requirements.txt

# Run server
uvicorn backend.app:app --reload --port 8000

# Open browser: http://localhost:8000
```

**Test with Docker:**
```bash
docker-compose up
# Visit http://localhost:8000
```

---

## 📁 FILES TO DEPLOY

### For Railway/Render (Full-Stack)
```
ritual-number-rush/
├── Dockerfile              ← Required
├── docker-compose.yml       ← Optional
├── backend/                ← Python source
├── frontend/index.html     ← Web UI
├── requirements.txt (inside backend/)
└── pyproject.toml          ← Optional
```

**All these files are already in the project directory.**

### For Static Hosting (Standalone)
Only need: `frontend/index-standalone.html`

---

## 🔧 DEPLOYMENT SCRIPTS

### Script 1: `deploy.sh` (Automated)
```bash
cd /tmp/hermes_sandbox_1z0b2pii/ritual-number-rush
chmod +x deploy.sh
./deploy.sh
```
*Requires `gh` CLI and `railway` CLI installed and logged in.*

### Script 2: `deploy-interactive.sh` (Helper)
```bash
cd /tmp/hermes_sandbox_1z0b2pii/ritual-number-rush
chmod +x deploy-interactive.sh
./deploy-interactive.sh
```
*Guides you through manual deployment.*

---

## 🌐 WHAT YOU GET

### Full-Stack Version
- ✅ Web UI accessible from any device
- ✅ Persistent leaderboard (SQLite)
- ✅ Multi-user support (shared DB)
- ✅ Share to Twitter
- ✅ REST API
- ✅ Docker containerization
- ✅ Free tier hosting available

### Standalone Version
- ✅ Single HTML file
- ✅ No server needed
- ✅ Works offline
- ✅ Can host on any static host
- ✅ Leaderboard per-browser (localStorage)
- ✅ Instant deployment

---

## 📊 FEATURES SHIPMENT

| Feature | Status | Notes |
|---------|--------|-------|
| Game logic | ✅ Complete | Tested locally |
| Leaderboard | ✅ Persistent | SQLite with stats |
| UI/UX | ✅ Responsive | Mobile-friendly |
| Docker | ✅ Configured | Multi-stage ready |
| API | ✅ RESTful | Extensible design |
| Deployment | ✅ Ready | Railway/Render compatible |

---

## 🎮 TESTING CHECKLIST

After deployment, verify:

- [ ] Page loads at live URL
- [ ] Start a game (input 1-100 range works)
- [ ] Guess numbers (higher/lower hints work)
- [ ] Win a game (score calculates correctly: 100 - attempts×10)
- [ ] Lose a game (shows correct number)
- [ ] Save score to leaderboard
- [ ] Leaderboard shows top 10
- [ ] Share to Twitter button works
- [ ] Mobile view test (resize browser)
- [ ] Game restart works

---

## ⚠️ TROUBLESHOOTING

**"Database locked" error**
→ Railway free tier has read-only filesystem. Fix: Switch to PostgreSQL or use Render.

**"No leaderboard entries"**
→ Fresh DB — just play some games!

**Port already in use**
→ Change port in `backend/app.py` (line `uvicorn.run(...)`) or Dockerfile

**Cannot reach Railway URL**
→ Wait 2-3 minutes for SSL provisioning
→ Check build logs in Railway dashboard

**Local: ModuleNotFoundError**
→ Did you run `pip install -r backend/requirements.txt`?

---

## 📈 NEXT ENHANCEMENTS (After Deploy)

1. **Ritual Wallet Integration**
   - Connect button using ethers.js
   - Sign score submission
   - On-chain leaderboard contract

2. **NFT Badges**
   - ERC-721 mint for top 10 players
   - Achievement system (first win, perfect game)

3. **Tournaments**
   - Scheduled events
   - Prize pool (RITUAL tokens)
   - Bracket system

4. **Multiplayer Mode**
   - WebSocket real-time
   - Head-to-head matches
   - ELO rating system

5. **Analytics Dashboard**
   - Most guessed numbers
   - Average win rate
   - Popular difficulty settings

---

## 🔗 QUICK LINKS

- **Project files:** `/tmp/hermes_sandbox_1z0b2pii/ritual-number-rush/`
- **Standalone HTML:** `frontend/index-standalone.html`
- **Full-stack entry:** `backend/app.py`
- **Deployment docs:** `DEPLOY.md`
- **Summary:** `SUMMARY.md`

---

## 📞 NEED HELP?

Check:
1. `DEPLOY.md` — detailed deployment steps
2. `README.md` — project overview
3. `SUMMARY.md` — feature breakdown

---

**🎯 Ready to launch. Choose your path:**

- **Path A (instant):** Open standalone HTML → Done in 10 seconds
- **Path B (professional):** Push to GitHub → Railway deploy → Live in 5 minutes
- **Path C (local):** `uvicorn backend.app:app --reload` → localhost:8000

**Pick Path B for maximum impact — shows full-stack skills + deployment chops.**
