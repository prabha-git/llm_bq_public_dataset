
import streamlit as st
from src.data_handler import get_table_schema_for_public_dataset, set_global_variables_bq_data_path
from src.config import DATASET_OPTIONS

from src.chatbot.agent.agent import langchain_agent

# Title of the app
st.title("Chicago Support")

# Sidebar for app description and image
st.sidebar.image("images/chicago2.jpg", caption="Chicago")
st.sidebar.markdown("""
    This app provides answers to questions based on below publicly available datasets from the City of Chicago:<br><br>
        <a href="https://data.cityofchicago.org/Public-Safety/Crimes-2001-to-Present/ijzp-q8t2" target="_blank">1. Chicago Crime dataset</a><br>
        <a href="https://data.cityofchicago.org/en/Administration-Finance/Current-Employee-Names-Salaries-and-Position-Title/n4bx-5kf6" target="_blank">2. City Employee Salary</a>
    """, unsafe_allow_html=True)



if "palm2_model" not in st.session_state:
    st.session_state["palm2_model"] = "chat-bison@001"

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

agent = langchain_agent()



if prompt := st.chat_input("Ask me about Chicago?"):
    st.session_state.messages.append({"role": "user", "content": prompt})

    with st.chat_message("user"):
        st.markdown(prompt)



    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        full_response = agent.ask_agent(prompt)
        st.markdown(full_response)

    st.session_state.messages.append({"role": "assistant", "content": full_response})


# #Code to test
# from src.chatbot.agent.agent import langchain_agent
# from src.data_handler import get_table_schema_for_public_dataset
# from langchain.globals import set_debug
# set_debug(True)

#
# agent = langchain_agent()
#print(agent.agent.agent.llm_chain.prompt.template)
# response = agent.ask_agent("How much crimes happened in chicago in 2023")







