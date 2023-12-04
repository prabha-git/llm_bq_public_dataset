import pandas as pd
import streamlit as st
from src.data_handler import get_table_schema_for_public_dataset, set_global_variables_bq_data_path
from src.config import DATASET_OPTIONS
from src.chatbot.agent.agent import langchain_agent
from src.utils import preprocess_text_for_markdown
import os
def setup_sidebar():
    st.sidebar.image("images/chicago2.jpg", caption="Chicago")
    st.sidebar.markdown("""
    This app provides answers to questions based on publicly available datasets from the City of Chicago:<br><br>
        <a href="https://data.cityofchicago.org/Public-Safety/Crimes-2001-to-Present/ijzp-q8t2" target="_blank">1. Chicago Crime dataset</a><br>
        <a href="https://data.cityofchicago.org/en/Service-Requests/311-Service-Requests-Request-Types/dgc7-2pdf" target="_blank">2. Chicago 311 Service Request</a>
    """, unsafe_allow_html=True)

def render_chat_message(message):
    role = message["role"]
    content = preprocess_text_for_markdown(message["content"])
    #content = message["content"]
    trace_route_url = message["trace_route"]
    with st.chat_message(role):
        st.markdown(content)
        if role != "user" :
            st.markdown(
                f"View trace in [🦜🛠️ LangSmith]({trace_route_url})",
                unsafe_allow_html=True,
            )

def display_chat_history(messages):
    for message in messages:
        render_chat_message(message)

def get_agent_response(agent,prompt):
    return agent.ask_agent(prompt)

def main():
    if "agent" not in st.session_state:
        st.session_state.agent = langchain_agent.get_instance()

    agent = st.session_state.agent

    st.title("Windy City Public Data Concierge")

    setup_sidebar()

    if "messages" not in st.session_state:
        st.session_state.messages = []

    display_chat_history(st.session_state.messages)

    prompt = st.chat_input("Ask me about Chicago?")
    if prompt:
        user_message = {"role": "user", "content": prompt,"trace_route":""}
        st.session_state.messages.append(user_message)
        render_chat_message(user_message)

        # Show a placeholder while processing
        with st.spinner('Please wait, processing...'):
            try:
                full_response,trace_route_url = get_agent_response(agent,prompt)
                assistant_message = {"role": "assistant", "content": full_response,"trace_route":trace_route_url}
                st.session_state.messages.append(assistant_message)
                render_chat_message(assistant_message)
            except Exception as e:
                st.error(f"An error occurred: {e}")
                # Optionally log the error
                # log_error(e)  # Implement this function as needed

if __name__ == "__main__":
    main()
