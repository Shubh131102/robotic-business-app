import streamlit as st
import cv2
import numpy as np

st.title("Path Planning Visualizer")

uploaded_file = st.file_uploader("Upload a map image", type=["png", "jpg", "jpeg"])

if uploaded_file is not None:
    file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
    image = cv2.imdecode(file_bytes, 0)

    st.image(image, caption="Uploaded Map", use_container_width=True)

