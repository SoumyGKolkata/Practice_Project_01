import streamlit as st
import requests

st.title("Simple AI App")

user_input = st.text_input("Enter your message:")

if st.button("Send"):
    response = requests.post(
        "http://127.0.0.1:8000/predict",
        json={"text": user_input}
    )

    if response.status_code == 200:
        st.write("AI:", response.json()["response"])
    else:
        st.write("Error connecting to API")