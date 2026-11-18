import streamlit as st
from src.image_processing import preprocess_image
from src.ocr import extract_text
st.set_page_config(page_title="Smart Bill AI",
page_icon="🧾",
layout="wide")
st.title("🧾 SMART BILL AI")
st.write("AI Powered intelligent bill organizer.")
st.subheader("Upload or Capture Your Bill")
uploaded_image=st.file_uploader("Upload your bill.",type=["jpg","jpeg","png"])

captured_image=st.camera_input("Capture your bill.")
if uploaded_image is not None:
    image = uploaded_image
elif captured_image is not None:
    image = captured_image
else:
    image = None

# if image is not None:
#     st.image(image, caption="Selected Bill", width=500)

if image is not None:

    st.image(image, caption="Original Bill", width=500)

    if st.button("Process Image"):

        grayscale, denoised, processed = preprocess_image(image)

        st.subheader("Image Processing Results")

        col1, col2, col3 = st.columns(3)

        with col1:
            st.image(grayscale, caption="Grayscale")

        with col2:
            st.image(denoised, caption="Denoised")

        with col3:
            st.image(processed, caption="Thresholded")

        
        st.subheader("Extracted Bill Text")#ocr text extraction

        extracted_text = extract_text(processed)

        st.text_area(
            "OCR Output",
            value=extracted_text,
            height=300
        )
