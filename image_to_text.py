import streamlit as st
import os
import google.generativeai as genai
import mimetypes

# Configure the Google Generative AI API
api = "AIzaSyCheCSgZiZfqU-Rv6KZFGUaEp2lrGkyfRI"
genai.configure(api_key=api)

# Function to upload a file to Gemini
def upload_to_gemini(path, mime_type=None):
    """Uploads the given file to Gemini."""
    file = genai.upload_file(path, mime_type=mime_type)
    return file

# Generation configuration
generation_config = {
    "temperature": 0.9,
    "top_p": 0.95,
    "top_k": 32,
    "max_output_tokens": 1024,
    "response_mime_type": "text/plain",
}

# Initialize the model
model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    generation_config=generation_config,
)

# Streamlit UI
st.title("Image Text Extraction with Google Generative AI")

# File upload
uploaded_file = st.file_uploader(
    "Upload an image (PNG, JPEG, JPG, BMP, GIF, TIFF):",
    type=["png", "jpeg", "jpg", "bmp", "gif", "tiff"]
)

if uploaded_file:
    # Save the uploaded file to a temporary location
    temp_path = os.path.join("temp", uploaded_file.name)
    os.makedirs("temp", exist_ok=True)
    with open(temp_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    st.success(f"File '{uploaded_file.name}' uploaded successfully!")

    # Determine MIME type of the uploaded file
    mime_type, _ = mimetypes.guess_type(temp_path)

    # Upload the file to Gemini and process it
    if st.button("Extract Text"):
        # st.info("Uploading file to Gemini and generating response...")
        try:
            gemini_file = upload_to_gemini(temp_path, mime_type=mime_type)
            
            # Generate content
            response = model.generate_content([
                gemini_file,
                "extract the text from the image, don't write any additional detail",
                "Image: extract the text from the image",
            ])
            
            # Display the extracted text
            st.subheader("Extracted Text:")
            st.text(response.text)
        except Exception as e:
            st.error(f"An error occurred: {e}")
