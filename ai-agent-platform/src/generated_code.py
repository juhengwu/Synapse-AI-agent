import streamlit as st
from PIL import Image
import io
import base64

# Function to generate base64 string for embedding images in the page
def img_to_base64_str(img_path):
    with open(img_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()

# Function to display an image with specified width using base64 string
def display_image(img_path, width=300):
    img_str = img_to_base64_str(img_path)
    st.markdown(
        f'<img src="data:image/png;base64,{img_str}" width="{width}">',
        unsafe_allow_html=True,
    )

# Function to display visual effects (placeholders for actual effects)
def display_visual_effects():
    st.write("### Visual Effect 1: Image Transition")
    display_image("path_to_transition_image.png")

    st.write("### Visual Effect 2: Interactive Slider")
    st.slider("Slide to interact", 0, 100, 50)

    st.write("### Visual Effect 3: Expanding Circles")
    display_image("path_to_circles_image.png")

# Streamlit UI components
st.title("Engaging Visual Effects with Streamlit")

st.header("Welcome to our cutting-edge visual effects showcase!")
st.write("Experience the creativity and technical prowess of our brand through engaging visual elements.")

# Display the visual effects in the app
display_visual_effects()

# Footer
st.write("---")
st.write("Thank you for visiting our visual effects showcase. We hope you enjoyed the experience!")