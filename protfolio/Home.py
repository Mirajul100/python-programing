import streamlit as st
import time

st.set_page_config(layout="wide")

time1 = time.strftime("%b:%d:%Y")
time2 = time.strftime("%H:%M:%S")

emcol , p_col , emcol1 = st.columns([ 9 , 9 , 5])

with emcol:
    st.subheader(time1)

with p_col:
    st.subheader("Mirajul Islam Anik")

with emcol1:
    st.subheader(time2)

col1 , empty_col ,col2 = st.columns([3, 0.2, 3])

with col1:
    st.image("protfolio/image.jpeg" , width=(600))

with col2:
    st.title("My Personal Information")
    st.info("Name : Mirajul Islam Anik")
    st.info(" Phon Number: 01747200359 ")
    st.info(" Phon Number: 01916269862 ")
    st.info(" Personal Email: mianikanikmatubbor@gmail.com")

with open ("protfolio/myInfo.txt","r") as file:
    st.info(file.read().title())

st.subheader("Below you can find my information. Feel free to contact me!")

col3 , empcol1 ,col4, empcol2, col5 = st.columns([2 , 0.6 ,2 , 0.6 , 2])

with col3:
    link = "[Link](https://github.com/Mirajul100)"
    st.image("protfolio/github.png")
    st.title("Git Hub Account")
    st.write(f"This is my git hub account link")
    st.write(link)

with col4:
    st.image("protfolio/google.png")
    st.title("Google Account")
    st.write("This is my google account")
    st.write("[Link](mirajulislamanik100@gmail.com)")

with col5:
    st.image("protfolio/linkedin.png")
    st.title("LinkedIn Account")
    st.write("This is my LinkedIn account")
    st.write("[Link](https://www.linkedin.com/in/anik-matubbor-mi-anik-3a5038358/)")
