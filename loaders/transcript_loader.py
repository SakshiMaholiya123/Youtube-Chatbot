from urllib.parse import urlparse, parse_qs

from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api._errors import (
    TranscriptsDisabled,
    NoTranscriptFound,
)


def extract_video_id(url: str) -> str:
  
    if "youtube.com" not in url and "youtu.be" not in url:
        return url.strip()

    parsed_url = urlparse(url)

    if parsed_url.netloc == "youtu.be":
        return parsed_url.path.lstrip("/")

    if "youtube.com" in parsed_url.netloc:
        query = parse_qs(parsed_url.query)

        if "v" in query:
            return query["v"][0]

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