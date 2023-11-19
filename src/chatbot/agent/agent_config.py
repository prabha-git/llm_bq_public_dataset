from langchain.agents.agent_types import AgentType
from langchain.memory import ConversationBufferMemory

from langchain.agents import Tool
from langchain.llms import VertexAI

from src.chatbot.tools.get_column_values import get_column_values
from src.chatbot.tools.execute_sql_and_get_results import execute_sql_and_get_results
from src.chatbot.tools.skip import skip
from src.chatbot.tools.get_all_dataset_info import get_all_dataset_info

PREFIX = """You are an agent who answers user questions by generating SQL and running it against BigQuery.

Available Tools (Use Only If Needed):
"""

FORMAT_INSTRUCTIONS = """Process Outline:

Question: Present the user's query.

Thought: Review available datasets and columns to assess if the query can be answered.

Action: Gell information for all the dataset

Action Input: No input reuired

Observation: You need to decide if the available table and columns can answer the question,  Conclude if the query is beyond the scope.

Thought: Based on the Question you need to decide if you need to use actual values in the SQL like in WHERE clause or CASE statement 

Action (If Needed): Use Get Column Values to obtain necessary column values for SQL.
    Input: Specify the column name or skip this step.

Observation: Note the outcome, whether column values were obtained or the step was skipped.

Thought: Select relevant column values for the SQL WHERE clause. Construct an SQL query to answer the user's question.

Action: Execute the SQL query using Execute SQL and Fetch Data.
    Input: The SQL query.

Observation: Note the results from the SQL query execution.

Thought: Conclude with the final answer to the user's query.
"""

FORMAT_INSTRUCTIONS1="""Use the following format:
Question: the input question you must answer
Thought: You need to understand Question and think how a SQL can be constructed.
Action: Get information of all dataset
Action Input: Dummy.
Observation: Decide if the tables and columns in the dataset are sufficient to answer the query. 
Thought: You need to think if actual column values are needed for SQL conditions.
Action: Use 'Get Column Values' if necessary.
Action Input: Specify the column name or skip this step.
Observation: Note whether necessary column values are obtained or if the step is skipped.
Thought: Construct an SQL query to address the user's query.
Action: Develop an SQL query.
Action Input: Information obtained from previous steps.
Observation: Formulate a query that aligns with the user's question and available data.
Thought: Execute the SQL query to fetch relevant data.
Action: Execute SQL and Fetch Data.
Action Input: The SQL query.
Observation: Analyze the results from the SQL query execution.
Thought: Formulate the final response based on the query results.
Action: Synthesize the answer.
Action Input: Results obtained from the SQL query.
Observation: Ensure the final response accurately addresses the user's question.
"""

memory = ConversationBufferMemory(memory_key="chat_history")

tools = [skip, get_column_values, execute_sql_and_get_results,get_all_dataset_info]
vertex_llm_model = VertexAI(
    model_name="code-bison-32k",
    temperature=0,
    max_output_tokens=4096,
    verbose=True
)

agent_parameters = {
    #'agent': AgentType.CONVERSATIONAL_REACT_DESCRIPTION,
    'agent':AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    'tools': tools,
    'llm': vertex_llm_model,
    'verbose': True,
    'max_iterations': 3,
    'handle_parsing_errors': True,
    #'memory': memory,
    'return_intermediate_steps':True
}
