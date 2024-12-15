import streamlit as st
from llm.controller import Controller
from utils.helper import get_text_from_pdfs

UPLOAD_DIR = "./data/files"
IMAGES_DIR = "./data/images"


def run(user_input, temperature, max_tokens):
    full_text = get_text_from_pdfs()

    for i in range(len(full_text)):
        full_text[i] = full_text[i].replace("\n", "   ")

    controller = Controller(temperature, max_tokens)

    col1, col2 = st.columns([7, 5])

    with col2:
        user_msg = st.chat_message("user")
        user_msg.write(user_input)

    assistant_message = st.chat_message("assistant")
    output_placeholder = assistant_message.empty()
    full_output = ""

    for token in controller.generate_response(user_input, full_text):
        full_output += token["choices"][0]["text"]
        output_placeholder.write(full_output)

    return full_output


# UI
st.subheader("RAG-CV", divider="gray")

assistant_message = st.chat_message("assistant")
assistant_message.write("How can I help you with your CV(s)?")
user_input = st.chat_input("Your query")

temperature = st.sidebar.slider("Temperature", 0.0, 1.0, 0.4, 0.01)
max_tokens = st.sidebar.slider("Max Tokens", 50, 1000, 500, 10)

if user_input:
    run(user_input, temperature, max_tokens)
