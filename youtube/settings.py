from django.conf import settings

ROOT_URLCONF = getattr(settings, 'ROOT_URLCONF', 'youtube.urls')

DEVELOPER_KEY = getattr(
    settings, 'GA_YOUTUBE_API_KEY', '')
YOUTUBE_API_SERVICE_NAME = getattr(
    settings, 'YOUTUBE_API_SERVICE_NAME', 'youtube')
YOUTUBE_API_VERSION = getattr(settings, 'YOUTUBE_API_VERSION', 'v3')
