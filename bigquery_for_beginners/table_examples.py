from google.cloud import bigquery

from secrets import settings


client = bigquery.Client()
dataset_id = "test_dataset"
table_id = f"{client.project}.{dataset_id}.test_table"


# Info: https://cloud.google.com/bigquery/docs/tables


def create_table():
    schema = [
        bigquery.SchemaField("name", "STRING", mode="REQUIRED"),
        bigquery.SchemaField("age", "INTEGER", mode="REQUIRED"),
    ]
    table = bigquery.Table(table_id, schema=schema)
    table = client.create_table(table)  # Make an API request.
    print(f"Created table {table.project}.{table.dataset_id}.{table.table_id}")


def table_info():
    table = client.get_table(table_id)  # Make an API request.

    print(f"Table schema: {table.schema}")
    print(f"Table description: {table.description}")
    print(f"Table has {table.num_rows} rows")


def select_data():
    sql = f"SELECT * FROM {table_id}"
    query_job = client.query(sql)
    res = query_job.result()
    print("Table data:")
    for i in res:
        print(f"\tName {i['name']}, age: {i['age']}")


def inser_data():
    data = [('John', 30), ('Snow', 32)]
    for name, age in data:
        sql = f"INSERT INTO {table_id} VALUES ('{name}', {age});"
        query_job = client.query(sql)
        query_job.result()
