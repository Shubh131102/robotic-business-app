import streamlit as st
import numpy as np
import cv2


st.title("Hello, Streamlit 👋")

st.write("Here's a simple example using OpenCV and NumPy.")

# Generate a dummy image with NumPy
img = np.zeros((300, 300, 3), dtype=np.uint8)
cv2.circle(img, (150, 150), 100, (255, 0, 0), -1)  # Draw a blue circle

# Display image in Streamlit
st.image(img, channels="BGR", caption="Generated with OpenCV")
