import streamlit as st
import function

studentName = function.readFile()

def add_student():
    student = st.session_state["newStudentName"] + "\n"
    studentName.append(student)
    function.writeFile(studentName)

st.title("Student management")

st.subheader("This is my student management system")
st.text_input (label="Enter name" , placeholder="Enter student name.." , 
               on_change=add_student , key="newStudentName")
st.write ("Select the student name")

for name in studentName:
    st.checkbox(name.title())

