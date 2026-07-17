from services.youtube_rag import process_video, ask_question

url = "https://youtu.be/Gfr50f6ZBvo"

print("Processing video...")

process_video(url)

print("Video processed successfully!")

print()

question = "What does Demis Hassabis say about AGI?"

answer = ask_question(question)

print(answer)