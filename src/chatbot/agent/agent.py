from langchain.agents import initialize_agent
from langchain.agents.format_scratchpad import format_to_openai_function_messages
from langchain.agents.output_parsers import OpenAIFunctionsAgentOutputParser

from src.chatbot.agent.agent_config import  llm_with_tools, prompt, tools
from langchain.agents import AgentExecutor
from langchain.callbacks import tracing_v2_enabled
from langsmith import Client
from langchain.schema.messages import AIMessage, HumanMessage


class langchain_agent:

    _instance = None

    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            cls._instance = cls()
        return cls._instance
    def __init__(self):
        self.agent = (
                {
                    "input": lambda x: x["input"],
                    "agent_scratchpad": lambda x: format_to_openai_function_messages(
                        x["intermediate_steps"]
                    ),
                    "chat_history": lambda x: x["chat_history"],
                }
                | prompt
                | llm_with_tools
                | OpenAIFunctionsAgentOutputParser()
        )
        self.agent_executor = AgentExecutor(agent=self.agent, tools=tools, verbose=True)
        self.chat_history=[]

    def ask_agent(self, q):
        langsmith_client = Client()
        with tracing_v2_enabled() as cb:
            answer = self.agent_executor.invoke({"input": q, "chat_history":self.chat_history})['output']
            self.chat_history.extend(
                [
                    HumanMessage(content=q),
                    AIMessage(content=answer)
                ]
            )
            latest_run_id = str(cb.latest_run.id)
            run_url = langsmith_client.share_run(run_id=latest_run_id)
            return answer, run_url
