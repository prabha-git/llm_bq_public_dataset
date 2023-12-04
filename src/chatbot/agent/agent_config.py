import os
from langchain.agents.agent_types import AgentType
from langchain.memory import ConversationBufferMemory

from langchain.agents import Tool
from langchain.llms import VertexAI
from langchain.chat_models import ChatOpenAI

from src.chatbot.tools.get_column_values import get_column_values
from src.chatbot.tools.execute_sql_and_get_results import execute_sql_and_get_results
from src.chatbot.tools.skip import skip
from src.chatbot.tools.get_all_dataset_info import get_all_dataset_info

from langchain.tools.render import format_tool_to_openai_function
from langchain.prompts import ChatPromptTemplate, MessagesPlaceholder


from dotenv import load_dotenv
load_dotenv()

from langchain.globals import set_debug
set_debug(True)

PREFIX = """You are a Chicago City Chat bot who answers user questions by generating SQL and running it against BigQuery.

You always answer based on the data in the tables.
You answer Only questions related to Chicago City.
You always follow the format below.
The information provided by user might not be directly used in the SQL, You need to use appropriate function to validate if the value exisit in the database before using it in the SQL. Some times it might exisist in different name so make a resonable assumption and explicitily state any assumption in the final answer.
If you need to run more than one query, run one at a time.
"""

FORMAT_INSTRUCTIONS="""Use the following format:

Question: the input question you must answer
Thought: You need to understand Question clearly.
Action: Get Information of all dataset
Action Input: Empty String
Observation: Output from the tool, Information about all the available dataset with table name and column descriptions.
Thought: You need to think if you can answer the question with the available dataset. You need to think if you need to know what the exact values in the column so that you can use it in SQL.
    [If not, skip everything else you need to think if actual values are needed to consutruct the SQL ( in WHERE clause or CASE statement)], You don't need to this for Date columns.
Action: Get Column Values [If needed]
Action Input: Input is in the format Project ID.Datset.table.column_name
Observation: Think how the values obtained would be used in the SQL or if the step is skipped.
Thought: You need to think and come up with a BigQuery SQL query to answer the Question, I need to look at dataset information to make sure column names and filter values are correct. If I need to run multiple queries , i need to to do one at a time.
Action: Execute SQL and fetch data
Action Input: Bigquery SQL in plain text, without any markdown or code block syntax. You need to use 'Get Column Values' function to validate any data values that you are using in SQL (Date and Time values are exemption)
    For example, SELECT * 
                    FROM dataset.table 
                    WHERE condition
Observation: Output from SQL execution. IF you get an error repeat this step considering the error message and if require rewrite the BigQuery SQL.
    [If you are getting Null values, make sure you are using correct Values and correct case  in filters,refer the dataset info or use 'Get Column Values' ]
[Repeat above steps util you get complete answer to the question]

Question: Think about the original question
Answer: Format the answer accordingly to convincingly answer the question. Use Markdown tables to present the results if needed.
"""


memory = ConversationBufferMemory(memory_key="chat_history")

tools = [get_column_values, execute_sql_and_get_results,get_all_dataset_info]
vertex_llm_model = VertexAI(
    model_name="text-bison-32k",
    temperature=0,
    max_output_tokens=4096,
    verbose=True
)

#oai_llm = ChatOpenAI(temperature=0, model_name='gpt-4-1106-preview',openai_api_key=os.getenv('OPENAI_API_KEY'))

oai_llm = ChatOpenAI(temperature=0, model_name='ft:gpt-3.5-turbo-1106:personal::8Q2DHBzV',openai_api_key=os.getenv('OPENAI_API_KEY'))

llm_with_tools = oai_llm.bind(functions = [format_tool_to_openai_function(t) for t in tools])

agent_parameters = {
    #'agent': AgentType.CONVERSATIONAL_REACT_DESCRIPTION,
    'agent':AgentType.CONVERSATIONAL_REACT_DESCRIPTION,
    'tools': tools,
    'llm': oai_llm,
    'verbose': True,
    'max_iterations': 10,
    'handle_parsing_errors': True,
    'memory': memory,
    'return_intermediate_steps':True
}

prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system", PREFIX + "\n\n"+ FORMAT_INSTRUCTIONS
        ),
        MessagesPlaceholder(variable_name="chat_history"),
        ("user", "{input}"),

        MessagesPlaceholder(variable_name="agent_scratchpad")
    ]
)