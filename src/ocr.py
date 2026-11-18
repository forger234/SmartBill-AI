import pytesseract


# Configure Tesseract executable location
pytesseract.pytesseract.tesseract_cmd = (
    r"C:\Program Files\Tesseract-OCR\tesseract.exe"
)


def extract_text(processed_image):

    # Extract text from the processed image
    extracted_text = pytesseract.image_to_string(
        processed_image,
        lang="eng"
    )

    return extracted_text