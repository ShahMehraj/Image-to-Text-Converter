```markdown
# Image Text Extraction with Google Generative AI

This Streamlit application enables users to extract text from uploaded images using **Google Generative AI**. Users can upload images in various formats, and the app processes the image to extract its textual content.

## Features

- Upload images in formats like PNG, JPEG, JPG, BMP, GIF, and TIFF.
- Extract text from uploaded images using the Google Generative AI (Gemini model).
- Display extracted text in a visually styled box within the app interface.
- User-friendly interface with a sidebar for uploading files.

---

## Installation

### Prerequisites

1. **Python 3.8 or later**: Ensure Python is installed on your system.
2. **Google Generative AI API Key**:
   - Obtain an API key from Google Generative AI.
   - Store it in a `.env` file in the project directory:
     ```
     GOOGLE_API_KEY=your_api_key_here
     ```

### Steps

1. Clone the repository:
   ```bash
   git clone https://github.com/your-repository/image-text-extraction.git
   cd image-text-extraction
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the Streamlit app:
   ```bash
   streamlit run app.py
   ```

---

## Usage

1. Open the app in your browser (usually at `http://localhost:8501`).
2. Use the **sidebar** to upload an image file.
3. Click the **Extract Text** button to start processing.
4. View the extracted text displayed in the main content area.

---

## File Structure

```
.
├── app.py              # Main application script
├── requirements.txt    # Required Python packages
├── .env                # API key for Google Generative AI 
└── README.md           # Project documentation
```

---

## Dependencies

The application requires the following Python packages:

- `streamlit`: For building the web interface.
- `google-generativeai`: To interact with Google Generative AI API.
- `python-dotenv`: For managing environment variables.
- `mimetypes`: For determining file types (standard library). 

Install these dependencies using the `requirements.txt` file:
```bash
pip install -r requirements.txt
```

---

## Troubleshooting

### Error: "module 'google.generativeai' has no attribute 'upload_file'"
- This error occurs if the `google.generativeai` library version does not support the `upload_file` method. Ensure you are using the correct version of the library.

### Missing `.env` File
- Ensure the `.env` file exists and contains the `GOOGLE_API_KEY`.
---


## Contributing

Feel free to submit issues or pull requests to improve this project. Contributions are welcome!

---

## Author

- **Your Name**
- GitHub: [your-github-handle](https://github.com/ShahMehraj)
```