from langchain_code import get_few_shot_db_chain
from streamlit import st

st.title("Retail chatbot")

question = st.text_input("Question : ")

if question:
    pass
