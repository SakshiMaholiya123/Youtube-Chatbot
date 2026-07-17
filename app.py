import streamlit as st

from services.youtube_rag import (
    process_video,
    ask_question,
)

# ----------------------------
# Page Configuration
# ----------------------------

st.set_page_config(
    page_title="YouTube RAG Chatbot",
    page_icon="🎥",
    layout="wide",
)

st.title("🎥 YouTube RAG Chatbot")
st.markdown(
    "Ask questions about any YouTube video."
)

st.divider()

# ----------------------------
# Session State
# ----------------------------

if "video_processed" not in st.session_state:
    st.session_state.video_processed = False

# ----------------------------
# YouTube URL
# ----------------------------

youtube_url = st.text_input(
    "Enter YouTube URL",
    placeholder="https://www.youtube.com/watch?v=..."
)

# ----------------------------
# Process Button
# ----------------------------

if st.button("Process Video", use_container_width=True):

    if not youtube_url.strip():
        st.warning("Please enter a YouTube URL.")
    else:

        with st.spinner("Processing video..."):

            process_video(youtube_url)

        st.session_state.video_processed = True

        st.success("Video processed successfully!")

st.divider()

# ----------------------------
# Question Section
# ----------------------------

question = st.text_input(
    "Ask a Question",
    placeholder="What is the main topic of this video?"
)

# ----------------------------
# Ask Button
# ----------------------------

if st.button("Ask Question", use_container_width=True):

    if not st.session_state.video_processed:
        st.warning("Please process a video first.")

    elif not question.strip():
        st.warning("Please enter a question.")

    else:

        with st.spinner("Generating answer..."):

            answer = ask_question(question)

        st.subheader("Answer")

        st.write(answer)