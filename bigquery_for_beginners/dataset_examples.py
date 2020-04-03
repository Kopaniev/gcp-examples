from google.cloud import bigquery

from secrets import settings


client = bigquery.Client()


def create_dataset():
    dataset_id = f"{client.project}.test_dataset"
    dataset = bigquery.Dataset(dataset_id)
    dataset.location = "US"
    dataset = client.create_dataset(dataset)

    print("Created dataset {}.{}".format(client.project, dataset.dataset_id))


def list_datasets():
    # https://cloud.google.com/bigquery/docs/listing-datasets
    print("Datasets:")
    for dataset in client.list_datasets():
        print(f"\t{dataset.dataset_id}")


def dataset_info(dataset_id):
    # https://cloud.google.com/bigquery/docs/dataset-metadata

    dataset_id = f"{client.project}.{dataset_id}"
    dataset = client.get_dataset(dataset_id)

    print("Description: {}".format(dataset.description))

    print("Labels:")
    labels = dataset.labels
    if labels:
        for label, value in labels.items():
            print(f"\t{label}: {value}")
    else:
        print("\tDataset has no labels defined.")

    print("Tables:")
    tables = list(client.list_tables(dataset))  # Make an API request(s).
    if tables:
        for table in tables:
            print(f"\t{table.table_id}")
    else:
        print("\tThis dataset does not contain any tables.")
