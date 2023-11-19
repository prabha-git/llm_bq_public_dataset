from google.cloud import bigquery


import dataset_infopy

project_id = "bigquery-public-data"
def get_bigquery_table_schema(project_id, dataset_id, table_id):
    client = bigquery.Client(project=project_id)

    # Use a string to reference the dataset and table
    dataset_ref = bigquery.DatasetReference(project_id, dataset_id)
    table_ref = dataset_ref.table(table_id)

    # Fetch the table
    table = client.get_table(table_ref)

    # Create a list to hold schema information
    schema_info = []

    # Iterate over the schema and append the name and data type of each column
    for schema_field in table.schema:
        column_info = f"{schema_field.name}: {schema_field.field_type}"
        schema_info.append(column_info)

    # Join the list into a single string, with each column on a new line
    return '\n'.join(schema_info)

def get_table_schema_for_public_dataset(public_dataset):

    dataset = dataset_infopy.public_dataset_info[public_dataset]['dataset']
    table_name = dataset_infopy.public_dataset_info[public_dataset]['table_name']

    return get_bigquery_table_schema(project_id,dataset,table_name)

