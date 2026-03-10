import streamlit as st
from rembg import remove
from PIL import Image
import io

# Page settings
st.set_page_config(page_title="AI Background Remover", page_icon="✂️", layout="centered")

# UI Title and Description
st.title("✂️ AI Background Remover")
st.markdown("Upload any photo and watch the AI completely remove the background in seconds!")

# File uploader (Drag & Drop supported)
uploaded_file = st.file_uploader("Choose a photo (Drag & Drop is supported)", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # 1. Prepare the original image to display
    original_image = Image.open(uploaded_file)

    st.write("### Processing... 🚀")

    # Create two columns for the "Wow" effect
    col1, col2 = st.columns(2)

    with col1:
        st.header("Original")
        st.image(original_image, use_container_width=True)

    # 2. Background removal process (The magic happens here)
    with st.spinner('AI is analyzing the background...'):
        result_image = remove(original_image)

    with col2:
        st.header("Result")
        st.image(result_image, use_container_width=True)

    # 3. Convert image to byte format for the download button
    buf = io.BytesIO()
    result_image.save(buf, format="PNG")
    byte_im = buf.getvalue()

    st.success("Success! 🎉")
    st.download_button(
        label="🖼️ Download Image (PNG)",
        data=byte_im,
        file_name="no_background.png",
        mime="image/png"
    )