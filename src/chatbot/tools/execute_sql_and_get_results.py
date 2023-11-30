import src.data_handler as dh
from langchain.tools import tool

@tool
def execute_sql_and_get_results(sql):
  """
  Run the SQL query and fetch results.
  """
  try:
    # Run the query
    query_result = dh.execute_bq_sql(sql)

    # Extract values into a list
    dataframe = query_result.to_dataframe()

    return dataframe
  except Exception as e:
    return f"An unexpected error occurred: {query_result}"