import os


def clean_data():
    voice_file = "src/notetaker/core/data/voice.wav"
    transcript_file = "src/notetaker/core/data/transcript.json"
    summary_file = "src/notetaker/core/data/summary.json"

    try: 
        os.remove(voice_file)
        print(f"The audio file was deleted successfully.")

    except FileNotFoundError: 
        print(f"The audio file was not found.")

    try: 
        os.remove(transcript_file)
        print(f"The transcript file was deleted successfully.")

    except FileNotFoundError: 
        print(f"The transcript file was not found.")

    try: 
        os.remove(summary_file)
        print(f"The summary file was deleted successfully.")

    except FileNotFoundError: 
        print(f"The summary file was not found.")