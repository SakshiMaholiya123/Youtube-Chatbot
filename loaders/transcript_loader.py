from urllib.parse import urlparse, parse_qs

from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api._errors import (
    TranscriptsDisabled,
    NoTranscriptFound,
)


def extract_video_id(url: str) -> str:
    """
    Extract the YouTube video ID from various URL formats,
    or return the input directly if it's already a video ID.
    """

    url = url.strip()

    # Already looks like a video ID
    if (
        "youtube.com" not in url
        and "youtu.be" not in url
    ):
        return url

    parsed = urlparse(url)

    # https://youtu.be/VIDEO_ID
    if "youtu.be" in parsed.netloc:
        return parsed.path.lstrip("/")

    # https://youtube.com/watch?v=VIDEO_ID
    if "youtube.com" in parsed.netloc:

        query = parse_qs(parsed.query)

        if "v" in query:
            return query["v"][0]

        # https://youtube.com/shorts/VIDEO_ID
        if "/shorts/" in parsed.path:
            return parsed.path.split("/shorts/")[1]

        # https://youtube.com/embed/VIDEO_ID
        if "/embed/" in parsed.path:
            return parsed.path.split("/embed/")[1]

        # https://youtube.com/live/VIDEO_ID
        if "/live/" in parsed.path:
            return parsed.path.split("/live/")[1]

    raise ValueError("Invalid YouTube URL")


def load_transcript(url: str):

    try:

        video_id = extract_video_id(url)

        api = YouTubeTranscriptApi()

        transcript = api.fetch(video_id)

        return transcript

    except TranscriptsDisabled:
        print("Transcript is disabled.")

    except NoTranscriptFound:
        print("No English transcript found.")

    except Exception as e:
        print(e)

    return []