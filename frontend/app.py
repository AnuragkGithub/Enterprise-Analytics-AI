import streamlit as st
import requests

st.title("STDatabuddy")

question = st.text_input("Ask question")

if question:

    response = requests.post(
        "http://localhost:8000/ask",
        json={"question":question}
    )

    data = response.json()

    st.write("Query ID:", data["query_id"])

    st.write(data["data"])