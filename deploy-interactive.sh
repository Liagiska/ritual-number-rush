#!/bin/bash
# Interactive Deployment Script for Ritual Number Rush
# This script helps you deploy manually step-by-step

echo "🎮 Ritual Number Rush - Deployment Helper"
echo "=========================================="
echo ""

# Check prerequisites
echo "📋 Checking prerequisites..."

# Check git
if ! command -v git &> /dev/null; then
    echo "❌ Git is not installed. Install from https://git-scm.com/"
    exit 1
fi
echo "✓ Git is installed"

# Check Docker (optional for local)
if command -v docker &> /dev/null; then
    echo "✓ Docker is available (for local testing)"
else
    echo "⚠ Docker not found (optional for local testing)"
fi

echo ""
echo "🚀 Deployment Options:"
echo "1. Deploy to Railway (Recommended - Free)"
echo "2. Deploy to Render (Free)"
echo "3. Deploy locally with Docker"
echo "4. Just show me the files"
echo ""
read -p "Choose option (1-4): " choice

case $choice in
    1)
        echo ""
        echo "⛵ Railway Deployment"
        echo "---------------------"
        echo "1. Go to https://railway.app and sign in"
        echo "2. Click 'New Project' → 'Deploy from GitHub'"
        echo "3. Connect your GitHub account if needed"
        echo "4. Search for repository: ritual-number-rush"
        echo "5. Click 'Deploy'"
        echo ""
        echo "Your app will be live at: https://ritual-number-rush.up.railway.app"
        echo ""
        echo "First, you need to push to GitHub. Press Enter to continue..."
        read
        ;;
    2)
        echo ""
        echo "🎨 Render Deployment"
        echo "--------------------"
        echo "1. Go to https://render.com"
        echo "2. Click 'New' → 'Web Service'"
        echo "3. Connect your GitHub repository"
        echo "4. Repository: ritual-number-rush"
        echo "5. Name: ritual-number-rush"
        echo "6. Region: Choose closest"
        echo "7. Branch: main"
        echo "8. Build Command: docker build -t ritual-game ."
        echo "9. Start Command: docker run -p 8000:8000 ritual-game"
        echo "10. Click 'Create Web Service'"
        echo ""
        read -p "Press Enter to continue..."
        ;;
    3)
        echo ""
        echo "🐳 Local Docker Deployment"
        echo "---------------------------"
        echo "Running: docker-compose up"
        echo ""
        cd "$(dirname "$0")"
        if command -v docker-compose &> /dev/null; then
            docker-compose up
        elif command -v docker &> /dev/null; then
            docker build -t ritual-game .
            docker run -p 8000:8000 -v $(pwd)/data:/app/data ritual-game
        else
            echo "❌ Docker not installed"
            exit 1
        fi
        ;;
    4)
        echo ""
        echo "📁 Files are ready in: $(pwd)"
        echo ""
        ls -la
        echo ""
        echo "Manual deployment:"
        echo "1. Create GitHub repo: https://github.com/new"
        echo "2. Push this directory"
        echo "3. Deploy to Railway/Render"
        ;;
esac

echo ""
echo "✅ Done!"
