import streamlit as st

# Define the title of the app
st.title("Basic Arithmetic Calculator")

# Define variables to store the input numbers
number1 = st.number_input("Enter first number", format="%f")
number2 = st.number_input("Enter second number", format="%f")

# Define a function to perform the arithmetic operations
def calculate(operation, num1, num2):
    try:
        if operation == 'add':
            return num1 + num2
        elif operation == 'subtract':
            return num1 - num2
        elif operation == 'multiply':
            return num1 * num2
        elif operation == 'divide':
            return num1 / num2
    except ZeroDivisionError:
        return "Cannot divide by zero!"

# Define UI elements for operations
operation = st.selectbox("Choose operation", ("add", "subtract", "multiply", "divide"))
calculate_button = st.button("Calculate")

# Perform the calculation and display the result when the button is clicked
if calculate_button:
    result = calculate(operation, number1, number2)
    st.success(f"The result is: {result}")