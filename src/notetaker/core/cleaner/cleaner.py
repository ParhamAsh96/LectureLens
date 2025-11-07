import os

def clean_data():
    transcript_file = "src/notetaker/core/data/transcript.json"
    summary_file = "src/notetaker/core/data/summary.json"

    try: 
        os.remove(transcript_file)
        print(f"File transcript deleted successfully.")

    except FileNotFoundError: 
        print(f"File transcript not found.")

    try: 
        os.remove(summary_file)
        print(f"File summary deleted successfully.")

    except FileNotFoundError: 
        print(f"File summary not found.")