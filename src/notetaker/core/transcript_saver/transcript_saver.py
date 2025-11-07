import json
from datetime import date


def save_transcript(course_name, lecture_title, full_text):
    transcript = {
        "Course": course_name,
        "Title": lecture_title,
        "Description": full_text,
        "Date": date.today().strftime("%d-%m-%Y")
    }

    with open("src/notetaker/core/data/transcript.json", "w", encoding="utf-8") as file:
        json.dump(transcript, file, ensure_ascii=False, indent=2)
    
    print("The transcript file was successfully saved.\n")
