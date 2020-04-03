from google.cloud import storage

import secrets.settings


def store_data_into_blob(bucket_name, blob_path, data):
    storage_client = storage.Client()
    bucket = storage_client.get_bucket(bucket_name)
    blob = bucket.blob(blob_path)
    blob.upload_from_string(data)
