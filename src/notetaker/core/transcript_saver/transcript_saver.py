import json
from datetime import date
from notetaker.core.speech_to_text.google_stt import transcribe_voice

full_text = transcribe_voice()


def save_transcript(full_text):
    transcript = {
        "Course": "Course name",
        "Title": "Lecture x",
        "Description": full_text,
        "Date": date.today().strftime("%d-%m-%Y")
    }

    with open("src/notetaker/core/data/transcript.json", "w", encoding="utf-8") as file:
        json.dump(transcript, file, ensure_ascii=False, indent=2)

save_transcript(full_text)