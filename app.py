import streamlit as st
from src.data_handler import get_table_schema_for_public_dataset, set_global_variables_bq_data_path
from src.config import DATASET_OPTIONS
from src.chatbot.agent.agent import langchain_agent
from src.utils import preprocess_text_for_markdown

# Title of the app
st.title("Windy City Public Data Concierge")

# Sidebar for app description and image
st.sidebar.image("images/chicago2.jpg", caption="Chicago")
st.sidebar.markdown("""
    This app provides answers to questions based on below publicly available datasets from the City of Chicago:<br><br>
        <a href="https://data.cityofchicago.org/Public-Safety/Crimes-2001-to-Present/ijzp-q8t2" target="_blank">1. Chicago Crime dataset</a><br>
        <a href="https://data.cityofchicago.org/Administration-Finance/Current-Employee-Names-Salaries-and-Position-Title/n4bx-5kf6" target="_blank">2. City Employee Salary</a>
    """, unsafe_allow_html=True)

# Initialize session state variables if they don't exist
if "palm2_model" not in st.session_state:
    st.session_state["palm2_model"] = "chat-bison@001"

if "messages" not in st.session_state:
    st.session_state.messages = []

# Create columns for layout
left_column, right_column = st.columns([3, 1])  # Adjust the ratio as needed

with left_column:
    # Display the chat messages in the left column
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(preprocess_text_for_markdown(message["content"]))

# Chat input is outside the columns so it spans the full width at the bottom
if prompt := st.chat_input("Ask me about Chicago?"):
    # Append the user's message immediately to the chat
    st.session_state.messages.append({"role": "user", "content": prompt})

    # Create a placeholder for the assistant's response
    assistant_message_placeholder = st.empty()

    # Display a temporary message to indicate that the bot is processing the request
    with assistant_message_placeholder.container():
        st.info("Please wait, processing...")

    # Call your agent to get the response
    agent = langchain_agent()
    full_response = agent.ask_agent(prompt)

    # Now update the placeholder with the actual response
    with assistant_message_placeholder.container():
        st.markdown(preprocess_text_for_markdown(full_response))

    # Append the assistant's message to the chat
    st.session_state.messages.append({"role": "assistant", "content": full_response})
