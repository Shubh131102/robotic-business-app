import streamlit as st
import cv2
import numpy as np

st.title("Path Planning Visualizer")

uploaded_file = st.file_uploader("Upload a map image", type=["png", "jpg", "jpeg"])

if uploaded_file is not None:
    file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
    image = cv2.imdecode(file_bytes, 0)  # Grayscale

    st.image(image, caption="Uploaded Map", use_container_width=True)

    # Use session state to store points
    if "start_point" not in st.session_state:
        st.session_state.start_point = None
    if "goal_point" not in st.session_state:
        st.session_state.goal_point = None

    # Ask user what they want to select
    select_mode = st.radio("Select Mode", ["Start Point", "Goal Point"])

    # Capture click
    clicked = st.image(image, caption="Click to select points", use_container_width=True)

    st.write("**Note:** Click functionality will be added soon in Day 2 Part 2.")  # We'll do clicks next
