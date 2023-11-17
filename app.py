
import streamlit as st
from src.data_handler import get_table_schema_for_public_dataset, set_global_variables_bq_data_path

from src.chatbot.agent.agent import langchain_agent

# Title of the app
st.title("Choose the Public Dataset")

# Dropdown menu in the sidebar for user input
options = ["Chicago Crime", "Austin Crime"]
selection = st.sidebar.selectbox("Choose the Public Dataset:", options)

# Update global variables of project_id, dataset, table_name
global_config = set_global_variables_bq_data_path(selection)

# Retrieve schema based on selection
schema = get_table_schema_for_public_dataset(selection)
agent = langchain_agent()


# Display the selection and schema in the center of the screen
st.write(f"<div style='text-align: center'>Your selection: <b>{selection}</b></div>", unsafe_allow_html=True)
st.write(f"<div style='text-align: center'>Schema: <b>{schema}</b></div>", unsafe_allow_html=True)
st.write(f"<div style='text-align: center'>Schema: <b>{agent.ask_agent('How much rows in this table')}</b></div>", unsafe_allow_html=True)
