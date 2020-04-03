import os


def service_key_init(service_key_path):
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = service_key_path
