import streamlit as st
import function

studentName = function.readFile()

def add_student():
    new_student = st.session_state["newStudent"] + "\n"
    studentName.append(new_student)
    function.writeFile(studentName)

st.title("Student management system")
st.text_input(label="Select the student name", 
              placeholder="Enter student name..", 
              on_change=add_student , key= "newStudent")

for index , name in enumerate(studentName):
    st.checkbox(f"{index + 1}..{name.title()}")