import os, math
from google.oauth2 import service_account
from google.cloud import storage
from google.api_core.exceptions import NotFound, Conflict


STORAGE_KEY_PATH = os.getenv("GOOGLE_STORAGE_CREDENTIALS", "./config/gcp-storage.json")
PROJECT_ID       = os.getenv("GCP_PROJECT", "notetaker-477400")
BUCKET_NAME      = os.getenv("GCS_BUCKET", "voice-data-bucket-12345")
LOCATION         = os.getenv("GCS_LOCATION", "EU")

creds = service_account.Credentials.from_service_account_file(STORAGE_KEY_PATH)
storage_client = storage.Client(credentials=creds, project=PROJECT_ID)

target_chunks = 64
min_chunk_mb = 8
max_chunk_mb = 64


def get_or_create_bucket(name, location):
    try:
        bucket = storage_client.get_bucket(name)
        print(f"Bucket already exists. Location: {bucket.location}")
        return bucket
    
    except NotFound:
        pass

    try:
        bucket = storage_client.create_bucket(name, location=location)
        print(f"Created bucket: {bucket.name} in {bucket.location}")
        return bucket
    
    except Conflict:
        bucket = storage_client.get_bucket(name)
        print(f"Bucket exists after conflict. Location: {bucket.location}")
        return bucket


def round_up_256kb(n_bytes):
    base = 256 * 1024
    return math.ceil(n_bytes / base) * base


def pick_chunk_size(voice_path, target_chunks, min_chunk_mb, max_chunk_mb):
    size = os.path.getsize(voice_path)
    
    if size == 0:
        return min_chunk_mb * 1024 * 1024

    min_chunk = min_chunk_mb * 1024 * 1024
    max_chunk = max_chunk_mb * 1024 * 1024

    ideal = max(size // max(1, target_chunks), min_chunk)
    ideal = min(ideal, max_chunk)

    return round_up_256kb(ideal)


def upload_to_bucket(blob_name, file_path, bucket_name):
    try:
        bucket = storage_client.get_bucket(bucket_name)
        blob = bucket.blob(blob_name)
        blob.upload_from_filename(file_path)
        print("The audio file was successfully uploaded.")
        return True
   
    except Exception as e:
        print(f"Upload failed: {e}")
        return False
    

def uplaod_voice():
    bucket = get_or_create_bucket(BUCKET_NAME, LOCATION)

    voice_path = r"src/notetaker/core/data/voice.wav"
    pick_chunk_size(voice_path, target_chunks, min_chunk_mb, max_chunk_mb)
    upload_to_bucket("lecture_voice", voice_path, bucket)