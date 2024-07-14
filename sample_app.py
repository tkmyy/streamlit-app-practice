import streamlit as st
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate


st.title("Translate (en → ja)")

if "messages" not in st.session_state:
    st.session_state["messages"] = [{"role": "assistant", "content": "How can I help you?"}]

for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

if user_input := st.chat_input():
    chat = ChatOpenAI(temperature=0, model_name="gpt-4o-2024-05-13")
    st.session_state.messages.append({"role": "user", "content": user_input})
    st.chat_message("user").write(user_input)
    system = (
        "You are a helpful assistant that translates {input_language} to {output_language}."
    )
    human = "{text}"
    prompt = ChatPromptTemplate.from_messages([("system", system), ("human", human)])
    chain = prompt | chat
    result = chain.invoke(
        {
            "input_language": "English",
            "output_language": "Japanese",
            "text": user_input,
        }
    )
    msg = result.content
    st.session_state.messages.append({"role": "assistant", "content": msg})
    st.chat_message("assistant").write(msg)
