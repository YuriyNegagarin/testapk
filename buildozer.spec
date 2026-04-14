[app]

# Название приложения — ученик меняет на своё
title = Моя Визитка

# Имя пакета (только латиница, без пробелов)
package.name = vizitka

# Домен (можно не менять)
package.domain = org.student

# Папка с исходниками
source.dir = .

# Какие файлы включать
source.include_exts = py,png,jpg,kv,atlas,ttf

# Версия приложения
version = 1.0

# Зависимости Python
requirements = python3,kivy

# Ориентация экрана
orientation = portrait

# Иконка приложения (если есть файл icon.png)
# icon.filename = %(source.dir)s/icon.png

# Android настройки
android.permissions = INTERNET
android.api = 33
android.minapi = 21
android.ndk = 25b
android.sdk = 33
android.accept_sdk_license = True

# Режим сборки
android.arch = arm64-v8a

[buildozer]
log_level = 2
warn_on_root = 1
