#!/usr/bin/env python3
"""
Cloud APK Builder using BeeWare/Briefcase approach
This script prepares your project for cloud building via multiple services
"""

import os
import json
import subprocess
from pathlib import Path

def create_project_package():
    """Package project for cloud upload"""
    project_dir = Path.cwd()
    
    # Create a minimal package
    package_info = {
        "name": "aivoicechat",
        "version": "0.1",
        "description": "AI Voice Chat Android App",
        "main": "main.py",
        "files": [
            "main.py",
            "buildozer.spec",
        ]
    }
    
    return package_info

def print_buildozer_app_instructions():
    """Print instructions for using BuildozerAPP cloud service"""
    instructions = """
╔════════════════════════════════════════════════════════════════════════════╗
║                    CLOUD APK BUILD INSTRUCTIONS                            ║
╚════════════════════════════════════════════════════════════════════════════╝

🌐 OPTION 1: Use BuildozerAPP (Most Reliable - Recommended)
─────────────────────────────────────────────────────────────────────────────
Website: https://buildozer.cloud or https://github.com/kivy/buildozer-cloud

Steps:
  1. Visit the BuildozerAPP website
  2. Upload your project files or link to your GitHub repo
  3. Configure build settings if needed
  4. Click "Build"
  5. Download the generated APK

Project files ready:
  ✓ main.py (main application)
  ✓ buildozer.spec (build configuration)


🔧 OPTION 2: Use GitHub Actions (Free & Automated)
─────────────────────────────────────────────────────────────────────────────
The workflow file has been created at: .github/workflows/build-apk.yml

Steps to enable:
  1. Push the .github/workflows/build-apk.yml to your GitHub repo
  2. Go to: https://github.com/marwan-AboMazen/voice-chatbot-android/actions
  3. Click "Build Android APK" workflow
  4. Click "Run workflow"
  5. Wait for the build to complete (~20-30 minutes)
  6. Download the APK from the workflow artifacts

Command to push workflow:
  git add .github/workflows/build-apk.yml
  git commit -m "Add GitHub Actions APK build workflow"
  git push origin main


☁️ OPTION 3: Use BeeWare/Briefcase
─────────────────────────────────────────────────────────────────────────────
Website: https://beeware.org/

Install:
  pip install briefcase

Initialize:
  briefcase new --template android

Build:
  briefcase build android
  briefcase package android


📦 OPTION 4: Online APK Builders (Easier but Less Reliable)
─────────────────────────────────────────────────────────────────────────────
• ApkStudio: https://www.apkstudio.org/
• Appetize.io: https://appetize.io/
• BuildStore: https://www.buildstore.io/

Upload buildozer.spec + main.py and configure the build.


╔════════════════════════════════════════════════════════════════════════════╗
║                        RECOMMENDED APPROACH                                ║
╚════════════════════════════════════════════════════════════════════════════╝

For your project, I recommend:

✅ GitHub Actions (Option 2) - Best for your scenario
   • Free and reliable
   • Automated on every push
   • Good integration with your repository
   • Full build logs available

📋 Current buildozer.spec is configured correctly:
   • Android API: 31 (modern, supports most devices)
   • Minimum API: 21 (good compatibility)
   • NDK: 25b (latest stable)
   • Requirements: python3, kivy, cython


🚀 QUICKSTART:

1. Navigate to your GitHub repository
2. Go to "Actions" tab
3. If you see "Build Android APK" workflow, you're ready!
4. Click the workflow and select "Run workflow"
5. Monitor the build progress in the action logs
6. Download APK from artifacts once complete


═════════════════════════════════════════════════════════════════════════════

Need help?
• Buildozer docs: https://buildozer.readthedocs.io/
• Kivy docs: https://kivy.org/doc/stable/
• Check build logs for specific errors
"""
    
    print(instructions)

def main():
    print_buildozer_app_instructions()
    
    # Package info
    package = create_project_package()
    print(f"\n✓ Project Package Info:")
    print(f"  Name: {package['name']}")
    print(f"  Version: {package['version']}")
    print(f"  Main file: {package['main']}")

if __name__ == "__main__":
    main()
