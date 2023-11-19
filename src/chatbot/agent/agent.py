from langchain.agents import  initialize_agent

from src.chatbot.agent.agent_config import PREFIX,FORMAT_INSTRUCTIONS1,agent_parameters

class langchain_agent:
    def __init__(self):
        self.agent = initialize_agent(**agent_parameters, agent_kwargs={
            'prefix': PREFIX,
            'format_instructions': FORMAT_INSTRUCTIONS1
        })


    def ask_agent(self,q):
        return self.agent(q)