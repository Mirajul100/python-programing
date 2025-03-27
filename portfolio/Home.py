import streamlit as st
import time

st.set_page_config(page_title="My Portfolio Website",layout="wide" , page_icon=("portfolio/Image/home.png"))

time1 = time.strftime("%b:%d:%Y")
time2 = time.strftime("%H:%M:%S")
st.divider()

emcol , p_col , emcol1 = st.columns([ 9 , 9 , 5])

st.divider()

with emcol:
    st.subheader(time1)

with p_col:
    st.subheader("Mirajul Islam Anik")

with emcol1:
    st.subheader(time2)

col1 , col2 = st.columns(2 , gap="medium" , vertical_alignment="center")

with col1:
    st.image("portfolio/Image/image.jpeg" , width=(600))

with col2:
    st.title("My Personal Information")
    st.info("Name : Mirajul Islam Anik")
    st.info(" Phon Number: 01747200359 ")
    st.info(" Phon Number: 01916269862 ")
    st.info(" Personal Email: mianikanikmatubbor@gmail.com")

st.divider()

with open ("portfolio/myInfo.txt","r") as file:
    st.info(file.read().title())

st.divider()

st.subheader("Below you can find my information. Feel free to contact me!")

st.divider()

col3 , col4, col5, col6 = st.columns(4 , gap="large" , vertical_alignment="bottom")

with col3:
    link = "[Link](https://github.com/Mirajul100)"
    st.image("portfolio/Image/github.png")
    st.title("Git Hub Account")
    st.write(f"This is my git hub account link")
    st.write(link)

with col4:
    st.image("portfolio/Image/google.png")
    st.title("Google  Account")
    st.write("This is my google account")
    st.write("[Link](mirajulislamanik100@gmail.com)")

with col5:
    st.image("portfolio/Image/linkedin.png")
    st.title("LinkedIn Account")
    st.write("This is my LinkedIn account")
    st.write("[Link](https://www.linkedin.com/in/anik-matubbor-mi-anik-3a5038358/)")

with col6:
    st.image("portfolio/Image/facebook.png")
    st.title("Facebook Account")
    st.write("This is my Facebook account")
    st.write("[Link](https://www.facebook.com/mionik.mionik.3)")

st.divider()