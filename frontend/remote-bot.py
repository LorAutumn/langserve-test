import streamlit as st
from langserve import RemoteRunnable

PIRATE_SPEAK_URL = "http://localhost:8000/pirate-speak"

pirate_speak_chain = RemoteRunnable(PIRATE_SPEAK_URL)

st.header("Chatbot Remote")

if "messages" not in st.session_state:
    st.session_state["messages"] = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Say something"):
    with st.chat_message("user"):
        st.markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})

    with st.chat_message("assistant"):
        assistant_message_stream = pirate_speak_chain.stream({"input": prompt})
        final_answer = ""
        message = st.empty()
        for token in assistant_message_stream:
            final_answer += token.content
            message.markdown(final_answer)
    st.session_state.messages.append(
        {"role": "assistant", "content": final_answer})
