import streamlit as st

st.set_page_config("My cv" , layout="centered" , page_icon="portfolio/Image/person.png")
content = "This is my Curriculum vitae"
st.title(content.title())
download = st.button("Curriculum Vitae")
if download:
    st.info("[Resume Link](https://drive.google.com/file/d/1OWRmbqiaS4EZsXh57Mf-Z88n8RV0oidu/view?usp=sharing)")
