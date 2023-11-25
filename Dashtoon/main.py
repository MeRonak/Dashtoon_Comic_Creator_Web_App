import streamlit as st
import requests
import streamlit_lottie as st_lottie
import json
import io
from PIL import Image

# Set page configuration
st.set_page_config(page_title="Comic Creator Web App", page_icon="💻", layout="wide")

# CSS for center aligning text
def center_align_text(text, font_size="20px"):
    styled_text = f"""
    <div style="
        text-align: center;
        font-size: {font_size};
    ">{text}</div>
    """
    return styled_text

# API Key
API_URL = "https://xdwvg9no7pefghrn.us-east-1.aws.endpoints.huggingface.cloud"
headers = {
    "Accept": "image/png",
    "Authorization": "Bearer VknySbLLTUjbxXAXCjyfaFIPwUTCeRXbFSOjwRiCxsxFyhbnGjSFalPKrpvvDAaPVzWEevPljilLVDBiTzfIbWFdxOkYJxnOPoHhkkVGzAknaOulWggusSFewzpqsNWM",
    "Content-Type": "application/json"
}

# Function to make API request
def query(payload):
    try:
        response = requests.post(API_URL, headers=headers, json=payload)
        response.raise_for_status()  # Raise an HTTPError for bad responses
        return response.content
    except requests.exceptions.HTTPError as err:
        st.error(f"Error: {err}")
    except requests.exceptions.RequestException as err:
        st.error(f"Error: {err}")
    except Exception as err:
        st.error(f"Unexpected error: {err}")

# Function to generate images based on text inputs using the Hugging Face API
def generate_images(comic_panels):
    images = []

    # Loop through each panel's text
    description = ""
    for i, panel_text in enumerate(comic_panels, start=1):
        # Make a request to the Hugging Face API to generate an image
        description += panel_text
        response = query({
            "inputs": description,
        })

        # Convert the image bytes to a PIL Image
        image = Image.open(io.BytesIO(response))

        # Append the generated image to the list
        images.append(image)

    return images

# Function to generate text input fields for comic panels
def generate_comic_panels(num_panels):
    comic_panels = []
    for i in range(1, num_panels + 1):
        panel_text = st.text_area(f"Panel {i} Text:")
        comic_panels.append(panel_text)
    return comic_panels

# Header Section
with st.container():
    left_column, right_column = st.columns((1, 1))
    with left_column:
        st.write("###")
        st.write("###")
        st.write("###")
        st.title("Create amazing comics using AI tools")
        st.write("We adore graphic novels. We had a strong desire to make comic strips. However, there was one issue. For nuts, some of us are incapable of drawing a straight line. Why, though, should that prevent us from making comics? Thus, this is a gift from us to the world at large: a comic creator.")
    with right_column:
        image = Image.open("Pictures/test.png")
        st.image(image, width=600)

# Instruction Section
with st.container():
    st.write("---")
    st.write("###")
    st.write("###")
    st.write("###")
    st.write("###")
    first, second, third = st.columns(3)
    with first:
        a = center_align_text("Enter the number of panels you want to", "30px")
        st.markdown(a, unsafe_allow_html=True)
        b = center_align_text("make sure to choose atleast 1 and atmost 10 panels")
        st.markdown(b, unsafe_allow_html=True)
        st.markdown(center_align_text("➡", "50px"), unsafe_allow_html=True)
    with second:
        c = center_align_text("Write the description", "30px")
        st.markdown(c, unsafe_allow_html=True)
        d = center_align_text("Write the description of each panel in front of space provided corresponding to each column, it can include description of character, scene, etc,.")
        st.markdown(d, unsafe_allow_html=True)
        st.markdown(center_align_text("➡", "50px"), unsafe_allow_html=True)
    with third:
        e = center_align_text("Click on Generate Comic", "30px")
        st.markdown(e, unsafe_allow_html=True)
        f = center_align_text("This step might take sometime to display results depending upon the number of panels")
        st.markdown(f, unsafe_allow_html=True)
        st.markdown(center_align_text("👨‍🎤🧑‍🎤👩‍🎤", "50px"), unsafe_allow_html=True)
    st.write("###")
    st.write("###")
    st.write("###")
    st.write("###")

# Comic Panel Generation Section
with st.container():
    st.write("---")
    num_panels = st.number_input("Enter the number of comic panels:", min_value=1, max_value=10, value=3)
    comic_panels = generate_comic_panels(num_panels)
    st.write("### Generated Comic Panels:")

    if st.button("Generate Comic"):
        # Call the generate_images function to get images based on the entered text
        generated_images = generate_images(comic_panels)
        # Display the generated images
        g = center_align_text("### Generated Comic Images:")
        st.markdown(g, unsafe_allow_html=True)
        for i, image in enumerate(generated_images, start=1):
            st.image(image, caption=f"Image for Panel {i}")
