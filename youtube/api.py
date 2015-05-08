from apiclient.discovery import build
from .settings import (
    DEVELOPER_KEY, YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION)


def youtube_search(search_term="", max_results=25):
    youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION,
                    developerKey=DEVELOPER_KEY)

    search_response = youtube.search().list(
        part="id,snippet",
        q=search_term,
        maxResults=max_results
    ).execute()

    return search_response
