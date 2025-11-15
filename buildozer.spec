[app]
title = AI Voice Chat [cite: 1]
package.name = aivoicechat [cite: 1]
package.domain = org.hallam [cite: 1]
icon.filename = %(source.dir)s/data/icon.png [cite: 1]
presplash.filename = %(source.dir)s/data/presplash.png [cite: 1]

version = 0.1 [cite: 1]
source.dir = . [cite: 1]
source.include_exts = py,png,jpg,kv,atlas,txt [cite: 2]

# *** IMPORTANT CHANGE: ADDED 'llama-cpp-python' ***
requirements = python3,kivy,cython,llama-cpp-python [cite: 2]

orientation = portrait [cite: 2]

android.permissions = INTERNET [cite: 2]
android.api = 31 [cite: 2]
android.minapi = 21 [cite: 2]
android.ndk = 25b [cite: 2]
android.accept_sdk_license = True [cite: 2]
android.bootstrap = sdl2 [cite: 2]
android.arch = arm64-v8a [cite: 2]

[buildozer]
log_level = 2 [cite: 2]
warn_on_root = 0 [cite: 2]
