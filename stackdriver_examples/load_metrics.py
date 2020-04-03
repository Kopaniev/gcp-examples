import json

from googleapiclient.discovery import build

from gcs_for_beginners.gcs_examples import store_data_into_blob
import secrets.settings


def get_metrics():
    project_id = secrets.settings.project_id
    project_name = f'projects/{project_id}'
    next_page_token = ""
    metrics = []

    service = build('monitoring', 'v3', cache_discovery=False)

    while True:

        metrics_resp = service.projects().metricDescriptors().list(
             name=project_name,
             pageSize=5000,
             pageToken=next_page_token
        ).execute()

        metrics_list = metrics_resp.get('metricDescriptors', [])
        metrics += [m['name'] for m in metrics_list]
        next_page_token = metrics_resp.get('nextPageToken')

        if not metrics_list or not next_page_token:
            break

    return metrics


if __name__ == '__main__':
    metrics = get_metrics()
    bucket_name = "load_logs_to_gcs"
    metrics_file_name = "stackdriver_metrics.json"
    store_data_into_blob(bucket_name, metrics_file_name, json.dumps(metrics))
