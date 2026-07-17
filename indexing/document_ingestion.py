from langchain_core.documents import Document

from loaders.transcript_loader import (
    extract_video_id,
    load_transcript,
)

from loaders.youtube_loader import (
    get_video_metadata,
)


def ingest_document(url: str) -> list[Document]:
   
    # Extract Video ID
    video_id = extract_video_id(url)

    # Fetch transcript
    transcript = load_transcript(video_id)

    # Fetch metadata
    metadata = get_video_metadata(video_id)

    # Merge all transcript snippets into one string
    full_transcript = "\n".join(
        chunk.text for chunk in transcript
    )

    document = Document(
        page_content=full_transcript,
        metadata={
            "video_id": video_id,
            "title": metadata.get("title"),
            "channel_title": metadata.get("channel_title"),
            "published_at": metadata.get("published_at"),
            "thumbnail": metadata.get("thumbnail"),
            "duration": metadata.get("duration"),
            "view_count": metadata.get("view_count"),
            "like_count": metadata.get("like_count"),
            "comment_count": metadata.get("comment_count"),
        },
    )

    return [document]