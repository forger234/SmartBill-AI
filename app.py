import streamlit as st
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

if image is not None:
    st.image(image, caption="Selected Bill", width=500)