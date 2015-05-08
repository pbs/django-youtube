from django.conf import settings

ROOT_URLCONF = getattr(settings, 'ROOT_URLCONF', 'youtube.urls')

DEVELOPER_KEY = getattr(
    settings, 'GOOGELE_DEVELOPER_KEY', "AIzaSyAodcHoCKVEv7t9782UE5-6PDw-z3Ls1ng")
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"
