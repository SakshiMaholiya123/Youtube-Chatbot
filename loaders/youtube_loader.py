import os

from dotenv import load_dotenv
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError


load_dotenv()

YOUTUBE_API_KEY = os.getenv("YOUTUBE_API_KEY")


def get_youtube_service():
    
    if not YOUTUBE_API_KEY:
        raise ValueError("YOUTUBE_API_KEY not found in .env file.")

    return build(
        serviceName="youtube",
        version="v3",
        developerKey=YOUTUBE_API_KEY
    )


def get_video_metadata(video_id: str) -> dict:

    try:
        youtube = get_youtube_service()

        request = youtube.videos().list(
            part="snippet,contentDetails,statistics",
            id=video_id
        )

        response = request.execute()

        if not response["items"]:
            raise ValueError("Video not found.")

        video = response["items"][0]

        snippet = video["snippet"]
        statistics = video.get("statistics", {})
        content = video["contentDetails"]

        metadata = {
            "video_id": video_id,
            "title": snippet.get("title"),
            "description": snippet.get("description"),
            "channel_title": snippet.get("channelTitle"),
            "published_at": snippet.get("publishedAt"),
            "thumbnail": snippet["thumbnails"]["high"]["url"],
            "duration": content.get("duration"),
            "view_count": statistics.get("viewCount", "0"),
            "like_count": statistics.get("likeCount", "0"),
            "comment_count": statistics.get("commentCount", "0")
        }

        return metadata

    except HttpError as e:
        print(f"YouTube API Error: {e}")

    except Exception as e:
        print(f"Error: {e}")

    return {}