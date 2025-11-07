import time
from notetaker.core.audio_recorder.recorder import record_voice
from notetaker.core.google_storage.voice_saver import uplaod_voice
from notetaker.core.speech_to_text.google_stt import transcribe_voice
from notetaker.core.transcript_saver.transcript_saver import save_transcript
from notetaker.core.summariser.openai_o3 import save_summary
from notetaker.core.publisher.notion_publisher import publish_notes
from notetaker.core.cleaner.cleaner import clean_data


def main():
    course_name = input("Please enter the name of the course: \n")
    lecture_title = input("Please enter the lecture title: \n")
    
    # Pipe-and-Filter Style

    # Filter 1
    record_voice()

    start = time.time()
    # Filter 2
    uplaod_voice()

    # Filter 3
    full_text = transcribe_voice()

    # Filter 4
    save_transcript(course_name, lecture_title, full_text)

    # Filter 5
    save_summary()

    # Filter 6
    publish_notes()

    # Filter 7
    clean_data()
    end = time.time()

    length = (end - start) / 60
    print(f"Operation duration: {length:.2f} minutes")


if __name__ == "__main__":
    main()