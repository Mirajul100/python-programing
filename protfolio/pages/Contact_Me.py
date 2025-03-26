import streamlit as st
from sendEmail import send_email

st.set_page_config(page_title="Contact Me" , layout="centered" , page_icon="protfolio/contract.png")

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
    st.success("Your email was sended successfully")