[app]
title = AI Voice Chat
package.name = aivoicechat
package.domain = org.hallam
icon.filename = %(source.dir)s/data/icon.png
presplash.filename = %(source.dir)s/data/presplash.png

version = 0.1
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,txt

requirements = python3,kivy,cython

orientation = portrait

android.permissions = INTERNET
android.api = 31
android.minapi = 21
android.ndk = 25b
android.accept_sdk_license = True
android.bootstrap = sdl2
android.arch = arm64-v8a

[buildozer]
log_level = 2
warn_on_root = 0
