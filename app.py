import os
from PIL import Image
import streamlit as st

def load_and_convert_images():
    # Streamlit file uploader for multiple image files
    uploaded_files = st.file_uploader(
        "Choose image files", 
        type=["jpeg", "jpg", "png", "bmp", "gif", "tiff"], 
        accept_multiple_files=True
    )

    if not uploaded_files:
        st.warning("No files uploaded.")
        return

    # Process each uploaded image file
    for uploaded_file in uploaded_files:
        try:
            # Load the image
            img = Image.open(uploaded_file)
            width, height = img.size
            rotated = False  # Flag to check if the image was rotated

            # Check if the image is in portrait mode (height > width)
            if height > width:
                # Rotate the image to landscape mode
                img = img.rotate(90, expand=True)
                rotated = True
                st.info(f"Image {uploaded_file.name} was rotated to landscape.")
            else:
                st.info(f"Image {uploaded_file.name} is already in landscape mode.")

            # Convert and save the image as JPG
            rgb_img = img.convert('RGB')  # Convert image to RGB to save as JPG
            new_file_name = f"{os.path.splitext(uploaded_file.name)[0]}.jpg"
            
            # Provide a download link for the converted image
            rgb_img.save(new_file_name, "JPEG")
            st.success(f"Converted and saved as: {new_file_name}")

            with open(new_file_name, "rb") as file:
                st.download_button(label="Download JPG", data=file, file_name=new_file_name, mime="image/jpeg")

        except Exception as e:
            st.error(f"Error processing the image {uploaded_file.name}: {e}")

if __name__ == "__main__":
    st.title("Image Converter")
    st.write("Upload images, and they will be rotated to landscape (if needed) and converted to JPG format.")
    load_and_convert_images()
