import streamlit as st
from PIL import Image

st.subheader("Image Converter")

file_upload = st.file_uploader("Upload Image")

with st.expander(label="Start camera"):
    camera_image = st.camera_input("Camera")

if camera_image:
    img = Image.open(camera_image)
    gray_image = img.convert("L")
    st.image(gray_image)

if file_upload:
    upload_img = Image.open(file_upload)
    gray_upload_image = upload_img.convert("L")
    st.image(gray_upload_image)