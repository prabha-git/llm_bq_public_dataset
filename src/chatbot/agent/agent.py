from langchain.agents import  initialize_agent
from langchain.agents.format_scratchpad import format_to_openai_function_messages
from langchain.agents.output_parsers import OpenAIFunctionsAgentOutputParser

from src.chatbot.agent.agent_config import PREFIX,FORMAT_INSTRUCTIONS2,llm_with_tools,prompt,tools
from langchain.agents import AgentExecutor

class langchain_agent:
    def __init__(self):
        self.agent = (
            {
                "input": lambda x: x["input"],
                "agent_scratchpad": lambda x: format_to_openai_function_messages(
                    x["intermediate_steps"]
                ),
            }
            | prompt
            | llm_with_tools
            | OpenAIFunctionsAgentOutputParser()
        )
        self.agent_executor = AgentExecutor(agent = self.agent, tools = tools, verbose= True)


    def ask_agent(self,q):
        return self.agent_executor.invoke({"input":q})