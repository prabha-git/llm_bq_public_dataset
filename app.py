
import streamlit as st
from src.data_handler import get_table_schema_for_public_dataset, set_global_variables_bq_data_path
from src.config import DATASET_OPTIONS

from src.chatbot.agent.agent import langchain_agent

# Title of the app
st.title("Chicago Support")

if "palm2_model" not in st.session_state:
    st.session_state["palm2_model"] = "chat-bison@001"

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("What is up?"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    agent = langchain_agent()

    with st.chat_message("assistant"):
        st.markdown(agent.ask_agent(prompt))
        # message_placeholder = st.empty()
        # full_response = ""
        # for response in client.chat.completions.create(
        #     model=st.session_state["openai_model"],
        #     messages=[
        #         {"role": m["role"], "content": m["content"]}
        #         for m in st.session_state.messages
        #     ],
        #     stream=True,
        # ):
        #     full_response += (response.choices[0].delta.content or "")
        #     message_placeholder.markdown(full_response + "▌")
        #message_placeholder.markdown(full_response)
    #st.session_state.messages.append({"role": "assistant", "content": full_response})

@st.cache_data
def fetch_schema_for_selcted_dataset(selection):
    try:
        return get_table_schema_for_public_dataset(selection)
    except Exception as e:
        st.error("Please select a correct dataset. Error: " + str(e))
        return None



##########################
#
# st.title("ChatGPT-like clone")
#
# client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])
#
# if "openai_model" not in st.session_state:
#     st.session_state["openai_model"] = "gpt-3.5-turbo"
#
# if "messages" not in st.session_state:
#     st.session_state.messages = []
#
# for message in st.session_state.messages:
#     with st.chat_message(message["role"]):
#         st.markdown(message["content"])
#
# if prompt := st.chat_input("What is up?"):
#     st.session_state.messages.append({"role": "user", "content": prompt})
#     with st.chat_message("user"):
#         st.markdown(prompt)
#
#     with st.chat_message("assistant"):
#         message_placeholder = st.empty()
#         full_response = ""
#         for response in client.chat.completions.create(
#             model=st.session_state["openai_model"],
#             messages=[
#                 {"role": m["role"], "content": m["content"]}
#                 for m in st.session_state.messages
#             ],
#             stream=True,
#         ):
#             full_response += (response.choices[0].delta.content or "")
#             message_placeholder.markdown(full_response + "▌")
#         message_placeholder.markdown(full_response)
#     st.session_state.messages.append({"role": "assistant", "content": full_response})

# To get the template
#print(agent.agent.agent.llm_chain.prompt.template)

# #Code to test
# from src.chatbot.agent.agent import langchain_agent
# from src.data_handler import get_table_schema_for_public_dataset
# from langchain.globals import set_debug
# set_debug(True)
#
# agent = langchain_agent()
# response = agent.ask_agent("How much crimes happened in chicago in 2023")







