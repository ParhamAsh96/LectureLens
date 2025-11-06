import io
from google.oauth2 import service_account
from google.cloud import storage
from google.cloud import speech


client_file = "src/notetaker/core/speech_to_text/stt_API2.json"
credentials = service_account.Credentials.from_service_account_file(client_file)
client = speech.SpeechClient(credentials=credentials)

""" For less than 60 sec
audio_file = "src/notetaker/core/speech_to_text/output.wav"
with io.open(audio_file, "rb") as f:
    content = f.read()
    audio = speech.RecognitionAudio(content=content)
"""

gcs_uri = "gcs:<uri link›"
config = speech.RecognitionConfig(
    encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
    sample_rate_hertz=16000,
    language_code="en-US",
    model="video"
)

audio = speech.RecognitionAudio(uri=gcs_uri)
operation = client.long_running_recognize(config=config, audio=audio)

# response = client.recognize(config=config, audio=audio) ---> For less than 60 sec

print("Waiting for operation to complete...")
response = operation. result(timeout=90)
print(response)