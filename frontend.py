# import streamlit for building the UI
import streamlit as st

# import requests to HTTP requests to the backend API
import requests

#title shown on the webpage
st.title("Simple calaulator(Frontend)")

# input box for the first number
num1 = st.number_input("Enter the first number")

# input box for the second number
num2 = st.number_input("Enter the second number")

# dropdown menu for selecting the operation
operation = st.selectbox("Select the operation", ["Add", "Subtract"])

# button to perform the calculation
if st.button("Calculate"):
    # decide which API endpoint to call
    if operation == "Add":
        url = "http://127.0.0.1:8000/add"
    else:
        url = "http://127.0.0.1:8000/sub"

    response = requests.get(url, params={"a": num1, "b": num2})
    result=response.json()
    st.success(f"The result is: {result['result']}")