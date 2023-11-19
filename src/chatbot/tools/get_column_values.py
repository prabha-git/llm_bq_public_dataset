from langchain.tools import tool
from langchain.agents import  Tool

from globals import get_global_variable

import src.data_handler as dh

# Define python function for tools
@tool("Get Column Values")
def get_column_values(bq_column):
  """
  Retrieves values from a specified BigQuery column, useful for SQL construction.
  """
  bq_project = get_global_variable('project_id')
  bq_dataset = get_global_variable('dataset')
  bq_table_name= get_global_variable('table_name')

  sql_query=f"""
  select distinct {bq_column} from {bq_project}.{bq_dataset}.{bq_table_name}
  """


  query_result = dh.execute_bq_sql(sql_query)

  # Extract values into a list
  unique_values = [row[0] for row in query_result]

  return unique_values

#get_column_values_func = Tool(name='Get Column Values', func=get_column_values, description="Useful when you want to find the values of a specific  column in BigQuery table,helpful when you want to construct the sql with where clause that required actual values. Input to this tool is BigQuery Column Name (bq_column)")

