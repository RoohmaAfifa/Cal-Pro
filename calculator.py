import streamlit as st

# Function to perform calculations
def calculate(num1, num2, operation):
    if operation == "Add":
        return num1 + num2
    elif operation == "Subtract":
        return num1 - num2
    elif operation == "Multiply":
        return num1 * num2
    elif operation == "Divide":
        return num1 / num2
    else:
        return "Invalid Operation"

# Streamlit UI
st.title("Simple Calculator")

num1 = st.number_input("Enter the first number", value=0.0)
num2 = st.number_input("Enter the second number", value=0.0)

operation = st.selectbox("Select Operation", ["Add", "Subtract", "Multiply", "Divide"])

if st.button("Calculate"):
    result = calculate(num1, num2, operation)
    st.write(f"The result of {operation} is: {result}")
