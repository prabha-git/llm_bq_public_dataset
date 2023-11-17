from langchain.agents.agent_types import AgentType

from langchain.agents import  Tool
from langchain.llms import VertexAI

from src.chatbot.tools.get_column_values import get_column_values
from src.chatbot.tools.execute_sql_and_get_results import execute_sql_and_get_results
from src.chatbot.tools.skip import skip

PREFIX = """You are an agent who answers user question by generating SQL and running it in BigQuery, consider the below table schema

Instructions:
Do not make things up while generating the SQL
If you need to know the exact values in a column to be used in WHERE clause or CASE statemnt, use 'Get Column Values' tool to get the values else skip this step.
Even if the user gives a value for filter or case statemnet, get the values of the column from the BigQuery table and reconsile with user request.


Schema of the table is below:

Table Name: bigquery-public-data.chicago_crime.crime
  name: unique_key, type: INTEGER,
  name: case_number, type: STRING,
  name: date, type: TIMESTAMP,
  name: block, type: STRING,
  name: iucr, type: STRING,
  name: primary_type, type: STRING,
  name: description, type: STRING,
  name: location_description, type: STRING,
  name: arrest, type: BOOLEAN,
  name: domestic, type: BOOLEAN,
  name: beat, type: INTEGER,
  name: district, type: INTEGER,
  name: ward, type: INTEGER,
  name: community_area, type: INTEGER,
  name: fbi_code, type: STRING,
  name: x_coordinate, type: FLOAT,
  name: y_coordinate, type: FLOAT,
  name: year, type: INTEGER,
  name: updated_on, type: TIMESTAMP,
  name: latitude, type: FLOAT,
  name: longitude, type: FLOAT,
  name: location, type: STRING

You have access to the following tools, use it only if needed:
"""



FORMAT_INSTRUCTIONS = """Use the following format:

Question: the input question you must answer
Thought: Based on the Question, determine if you need to know the values of a specific column in a table, for example, to use in a WHERE clause or CASE statement. if yes, you need to use the tool  "Get Unique values for a column".
Action: the action to take, use the tool "Get Unique values for a column" or skip it.
Action Input: the input to the action is the column name for whic you want the values or skip it
Observation: the result of the action
Thought: Using your knowledge, select the appropriate values from  the actual  column values to construct the sql WHERE clause that aligns with Question, if not applicable create a SQL to answer the Question
Action: Execute the Final SQL and fetch data
Action Input: Correctly formatted SQL from the Final Answer
Observation: the result of the action
Thought: I now know the final answer
"""

#get_column_values_func = Tool(name='Get Column Values', func=get_column_values, description="Useful when you want to find the values of a specific  column in BigQuery table,helpful when you want to construct the sql with where clause that required actual values. Input to this tool is BigQuery Column Name (bq_column)")
#execute_sql_and_get_results_func = Tool(name='Execute the Final SQL and fetch data', func=execute_sql_and_get_results, description="Useful when you want to execute the final SQL and fetch the results, Input to this tool sql query")

tools = [skip,get_column_values,execute_sql_and_get_results]
vertex_llm_model = VertexAI(
  model_name="code-bison-32k",
  temperature=0,
  max_output_tokens=4096,
  verbose=True
)

agent_parameters = {
    'agent':AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    'tools':tools,
    'llm':vertex_llm_model,
    'verbose':True,
    'max_iterations':3,
    'return_intermediate_steps':True,
    'early_stopping_method':'generate',
  'handle_parsing_errors':True,
}

