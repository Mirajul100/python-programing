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
    st.subheader("My Personal Information")
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
    st.image("portfolio/Image/github.png")
    st.title("Git Hub Account")
    st.write(f"This is my git hub account link")
    st.link_button(label=("Github Link") 
                   ,url=("https://github.com/Mirajul100") 
                   ,use_container_width=(True)
                   ,type="secondary" , help=("github link"))

with col4:
    st.image("portfolio/Image/google.png")
    st.title("Google  Account")
    st.write("This is my google account")
    st.link_button(label=("Google Link") , url=("mirajulislamanik100@gmail.com")
                   ,help=("google account link") , use_container_width=(True))

with col5:
    st.image("portfolio/Image/linkedin.png")
    st.title("LinkedIn Account")
    st.write("This is my LinkedIn account")
    st.link_button(label="Linkedin Link" 
                   ,url="https://www.linkedin.com/in/anik-matubbor-mi-anik-3a5038358/"
                   ,help="linked account link", use_container_width=(True))

with col6:
    st.image("portfolio/Image/facebook.png")
    st.title("Facebook Account")
    st.write("This is my Facebook account")
    st.link_button(label="Facebook Link"
                   ,url="https://www.facebook.com/mionik.mionik.3"
                   ,help="facebook account link",use_container_width=(True))

st.divider()

col7 , col8 , col9 = st.columns(3 , gap="medium" , vertical_alignment="bottom")

with col7:
    st.image("portfolio/Image/1.png")
    st.title("Name todo list")
    st.link_button(label="Todo List Link"
                   ,url=("https://github.com/Mirajul100/python-programing/tree/master/Web")
                   ,help="todo list link",use_container_width=(True))

with col8:
    st.image("portfolio/Image/3.png")
    st.title("PDF converter")
    st.link_button(label="PDF Converter Link"
                   ,url=("https://github.com/Mirajul100/python-programing/tree/master/pdf")
                   ,help="pdf converter link",use_container_width=(True))

with col9:
    st.image("portfolio/Image/4.png")
    st.title("XL to PDF converter")
    st.link_button(label="XL to PDF Converter Link"
                   ,url=("https://github.com/Mirajul100/python-programing/tree/master/invoices")
                   ,help="xl to pdf converter link",use_container_width=(True))

st.divider()