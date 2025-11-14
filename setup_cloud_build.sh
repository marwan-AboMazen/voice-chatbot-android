#!/bin/bash
# Cloud Build Setup Script
# This script prepares your project for cloud building via GitHub Actions

set -e

echo "╔═══════════════════════════════════════════════════════════════╗"
echo "║        Voice Chatbot Android - Cloud Build Setup             ║"
echo "╚═══════════════════════════════════════════════════════════════╝"
echo ""

PROJECT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$PROJECT_DIR"

echo "✓ Project directory: $PROJECT_DIR"
echo ""

# Check if git repository exists
if [ ! -d .git ]; then
    echo "❌ Error: Not a git repository"
    echo "   Please run this from your git repository root"
    exit 1
fi

echo "✓ Git repository found"
echo ""

# Check git remote
REMOTE_URL=$(git config --get remote.origin.url)
echo "✓ Remote repository: $REMOTE_URL"
echo ""

# Verify key files exist
echo "Checking required files:"
for file in buildozer.spec main.py .github/workflows/build-apk.yml; do
    if [ -f "$file" ]; then
        echo "  ✓ $file"
    else
        echo "  ❌ Missing: $file"
    fi
done
echo ""

# Show configuration
echo "Current build configuration:"
echo "  • App: $(grep 'title =' buildozer.spec | cut -d'=' -f2 | xargs)"
echo "  • Package: $(grep 'package.name =' buildozer.spec | cut -d'=' -f2 | xargs)"
echo "  • Android API: $(grep 'android.api =' buildozer.spec | cut -d'=' -f2 | xargs)"
echo "  • Minimum API: $(grep 'android.minapi =' buildozer.spec | cut -d'=' -f2 | xargs)"
echo "  • NDK: $(grep 'android.ndk =' buildozer.spec | cut -d'=' -f2 | xargs)"
echo ""

echo "╔═══════════════════════════════════════════════════════════════╗"
echo "║                   READY FOR CLOUD BUILD!                     ║"
echo "╚═══════════════════════════════════════════════════════════════╝"
echo ""
echo "Next steps:"
echo "  1. Commit and push your changes:"
echo ""
echo "     git add .github/workflows/build-apk.yml buildozer.spec"
echo "     git commit -m 'Prepare for cloud build'"
echo "     git push origin main"
echo ""
echo "  2. Visit GitHub Actions:"
echo "     https://github.com/marwan-AboMazen/voice-chatbot-android/actions"
echo ""
echo "  3. Run the 'Build Android APK' workflow"
echo ""
echo "  4. Download your APK from the artifacts"
echo ""
echo "Build will take approximately 20-30 minutes ⏱️"
echo ""
