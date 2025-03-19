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

st.subheader("Select the student name to deleted")

for index , name in enumerate(studentName):
    checkBox = st.checkbox(f"{index + 1} . {name.title()}", 
                           key=name)
    if checkBox:
        studentName.pop(index)
        function.writeFile(studentName)
        del st.session_state[name]
        st.rerun()
