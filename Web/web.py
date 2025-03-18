import streamlit as st
import function

st.title("Student management")

st.subheader("This is my student management system")
st.write ("Select the student name")
st.text_input (label="Enter name" , placeholder="Enter student name..")

for name in function.readFile():
    st.checkbox(name.title())

