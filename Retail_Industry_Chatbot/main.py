from langchain_code import get_few_shot_db_chain
import streamlit as st

st.title("Retail chatbot 👕")

question = st.text_input("Question : ")

if question:
    chain = get_few_shot_db_chain()
    response = chain.run(question)

    st.header("Answer")
    st.write(response)
