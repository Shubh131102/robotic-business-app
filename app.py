import streamlit as st
import cv2
import numpy as np
import tempfile

st.title("Path Planning Visualizer")

uploaded_file = st.file_uploader("Upload a map image", type=["png", "jpg", "jpeg"])

if uploaded_file is not None:
    file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
    image = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)  # Read as color for line drawing

    st.image(image, caption="Uploaded Map", use_container_width=True)

    st.subheader("Select Points")

    col1, col2 = st.columns(2)

    with col1:
        start_x = st.number_input("Start X", min_value=0, max_value=image.shape[1]-1, value=0)
        start_y = st.number_input("Start Y", min_value=0, max_value=image.shape[0]-1, value=0)

    with col2:
        goal_x = st.number_input("Goal X", min_value=0, max_value=image.shape[1]-1, value=image.shape[1]-1)
        goal_y = st.number_input("Goal Y", min_value=0, max_value=image.shape[0]-1, value=image.shape[0]-1)

    if st.button("Draw Path"):
        # Draw a red line between Start and Goal
        image_with_path = image.copy()
        cv2.line(image_with_path, (int(start_x), int(start_y)), (int(goal_x), int(goal_y)), (0, 0, 255), thickness=2)

        st.image(image_with_path, caption="Path Drawn", use_container_width=True)
