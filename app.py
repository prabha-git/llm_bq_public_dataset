
import streamlit as st
from src.data_handler import get_table_schema_for_public_dataset, set_global_variables_bq_data_path
from src.config import DATASET_OPTIONS

from src.chatbot.agent.agent import langchain_agent

# Title of the app
st.title("Choose the Public Dataset")

# Dropdown menu in the sidebar for user input
selection = st.sidebar.selectbox("Choose the Public Dataset:", DATASET_OPTIONS)

# Update global variables of project_id, dataset, table_name
global_config = set_global_variables_bq_data_path(selection)

@st.cache_data
def fetch_schema_for_selcted_dataset(selection):
    try:
        return get_table_schema_for_public_dataset(selection)
    except Exception as e:
        st.error("Please select a correct dataset. Error: " + str(e))
        return None

# Retrieve schema based on selection
selected_dataset_schema = fetch_schema_for_selcted_dataset(selection)



agent = langchain_agent()


# Display the selection and schema in the center of the screen
st.write(f"<div style='text-align: center'>Your selection: <b>{selection}</b></div>", unsafe_allow_html=True)
st.write(f"<div style='text-align: center'>Schema: <b>{selected_dataset_schema}</b></div>", unsafe_allow_html=True)
st.write(f"<div style='text-align: center'>Schema: <b>{agent.ask_agent('How much rows in this table')}</b></div>", unsafe_allow_html=True)
