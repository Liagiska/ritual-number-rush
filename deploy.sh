#!/bin/bash
# Deploy Ritual Number Rush to Railway
# Run this script from the project root directory

set -e

echo "🚀 Deploying Ritual Number Rush..."

# Check if git is installed
if ! command -v git &> /dev/null; then
    echo "❌ Git is not installed"
    exit 1
fi

# Check if gh CLI is installed
if ! command -v gh &> /dev/null; then
    echo "❌ GitHub CLI (gh) is not installed"
    echo "Install from: https://cli.github.com/"
    exit 1
fi

# Check if logged in to GitHub
if ! gh auth status &> /dev/null; then
    echo "❌ Not logged in to GitHub. Run: gh auth login"
    exit 1
fi

# Check if logged in to Railway
if ! railway login &> /dev/null; then
    echo "❌ Not logged in to Railway. Run: railway login"
    exit 1
fi

# Initialize git if not already
if [ ! -d ".git" ]; then
    echo "📝 Initializing git repository..."
    git init
    git add .
    git config user.email "hermes@ritual.dev"
    git config user.name "Hermes Meong"
    git commit -m "Initial commit - Ritual Number Rush"
fi

# Create GitHub repo
echo "🌐 Creating GitHub repository..."
gh repo create ritual-number-rush --public --source=. --remote=origin || true

# Push to GitHub
echo "📤 Pushing to GitHub..."
git push -u origin main || git push -f origin main

# Link to Railway
echo "🚂 Linking to Railway..."
# Check if Railway project exists
if railway link 2>/dev/null; then
    echo "✓ Linked to existing Railway project"
else
    echo "✨ Creating new Railway project..."
    railway init --name ritual-number-rush --template docker
fi

# Deploy
echo "🔧 Deploying to Railway..."
railway up

echo "✅ Deployment complete!"
echo ""
echo "Your app will be available at:"
echo "https://ritual-number-rush.up.railway.app"
echo ""
echo "To view logs: railway log"
echo "To open in browser: railway open"
