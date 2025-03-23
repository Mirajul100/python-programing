import streamlit as st
from sendEmail import send_email

st.title("Contact Me")

with st.form(key="email_form"):
    user_email = st.text_input("Your Email Address", placeholder=("Enter Email Address..."))
    raw_message = st.text_area("Your Message" , placeholder=("Enter Message..."))
    message = f"""\
Subject: Protfolio New email from {user_email}

From:{user_email}
{raw_message}
"""
    button = st.form_submit_button("Submit")

if button:
    send_email(message)
    st.info("Your email was sended successfully")