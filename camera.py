import streamlit as st
from PIL import Image

with st.expander("start camera"):
    image = st.camera_input("Camera")

if image:
    img = Image.open(image)

    gray_image = img.convert("L")

    st.image(gray_image)