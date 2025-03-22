import streamlit as st

st.set_page_config(layout="wide")

col1 ,col2 = st.columns(2)

with col1:
    st.image("protfolio/image.jpeg")

with col2:
    st.title("Mirajul Islam Anik")
    content = """Hello my name is Mirajul Islam Anik. I am studied at 
    Daffodil international university in Bsc in CSE"""
    st.info(content.title())

st.subheader("Below you can find my information. Feel free to contact me!")

col3 , col4 , col5 = st.columns(3)

with col3:
    st.image("protfolio/github.png")
    st.title("Git Hub Account")
    st.write("This is my git hub account link")
    st.write("https://github.com/Mirajul100")

with col4:
    st.image("protfolio/google.png")
    st.title("Google Account")
    st.write("This is my google account")
    st.write("mirajulislamanik100@gmail.com")

#with col5:
   # st.image()
