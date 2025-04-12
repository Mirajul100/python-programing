import streamlit as st
from sendEmail import send_email

st.set_page_config(page_title="Contact Me" , layout="centered" , page_icon="portfolio/Image/contract.png")

st.title("Contact Me")

with st.form(key="email_form"):
    user_email = st.text_input("Your Email Address", placeholder=("Enter Email Address..."))
    st.divider()
    raw_message = st.text_area("Your Message" , placeholder=("Enter Message..."))
    st.divider()
    message = f"""\
Subject: Portfolio New email from {user_email}

From:{user_email}
{raw_message}
"""
    button = st.form_submit_button("Submit" , use_container_width=(True))

if button:
    send_email(message)
    st.success("Your email was sended successfully")