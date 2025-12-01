import streamlit as st
import calculator as calc

st.title("✨Simple Calculator (Task 8) 🧮")

num1 = st.number_input("Enter first number", value=0.0)
num2 = st.number_input("Enter second number", value=0.0)

operation = st.selectbox(
    "Select Operation",
    ["Add", "Subtract", "Multiply", "Divide"]
)

if st.button("Calculate"):
    if operation == "Add":
        result = calc.add(num1, num2)
    elif operation == "Subtract":
        result = calc.subtract(num1, num2)
    elif operation == "Multiply":
        result = calc.multiply(num1, num2)
    elif operation == "Divide":
        result = calc.divide(num1, num2)

    st.success(f"Result: {result}")