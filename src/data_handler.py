
from src.dataset_info import public_dataset_info
from google.cloud import bigquery
from globals import update_global_variable, get_global_variable
from globals import config

# Setting the global variables
project_id = get_global_variable('project_id')
dataset = get_global_variable('dataset')
table_name = get_global_variable('table_name')

def create_bigquery_client(project_id):
    return bigquery.Client(project=project_id)

def get_bigquery_table_schema(project_id, dataset_id, table_id):
    client = create_bigquery_client(project_id=project_id)

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

def get_table_schema_for_public_dataset(dataset_name):
    # This function retrieves the schema for the selected public dataset
    return get_bigquery_table_schema(get_global_variable('project_id'),
                                         get_global_variable('dataset'),
                                         get_global_variable('table_name'))


def set_global_variables_bq_data_path(dataset_name):
    dataset_info = public_dataset_info.get(dataset_name, {})
    update_global_variable('project_id',new_value=dataset_info['project_id'])
    update_global_variable('dataset', new_value=dataset_info['dataset'])
    update_global_variable('table_name', new_value=dataset_info['table_name'])



def execute_bq_sql(sql):
    project_id = 'genai-prabha-learn'
    try:
        client = create_bigquery_client(project_id=project_id)
        query_job = client.query(sql)
        # Fetch the results
        results = query_job.result()
        return results
    except Exception as e:
        # Handle other exceptions
        return f"An unexpected error occurred: {e}"

