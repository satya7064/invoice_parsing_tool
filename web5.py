import datetime
import streamlit as st  #Web App
import requests
import os
import basic_OCR
import aspose.words as aw
from PIL import Image

st.set_page_config(layout="wide")
image = Image.open(r'BPAI_logo.png')
st.image(image)
st.title("INVOICE PARSING")
input_file = st.file_uploader(label='UPLOAD PDF FILE HERE:', type=['pdf','doc','docx'])

if input_file is not None:
    if input_file.type == "application/pdf":
        with open(os.path.join("uploaded_files", input_file.name),"wb") as f:
                f.write((input_file).getbuffer())
        pdf_file = os.path.join("./uploaded_files/", input_file.name)
        data = basic_OCR.result_data(pdf_file)
        st.success("Invoice Data Extracted Successfully")
        st.write(data)  # Display the extracted data in the Streamlit web page
        if st.button("Download Results"):  # Add a download button
            with open("extracted_data.txt", "w") as f:
                f.write(data)
            st.markdown("File downloaded!")
            st.markdown("<a href='extracted_data.txt' download>Download Results</a>", unsafe_allow_html=True)
        
    else:
        doc = aw.Document(input_file)
        doc.save("./uploaded_files/temp.pdf")
        data = basic_OCR.result_data('./uploaded_files/temp.pdf')
        st.success("Invoice Data Extracted Successfully")
        st.write(data)  # Display the extracted data in the Streamlit web page
        if st.button("Download Results"):  # Add a download button
            with open("extracted_data.txt", "w") as f:
                f.write(data)
            st.markdown("File downloaded!")
            st.markdown("<a href='extracted_data.txt' download>Download Results</a>", unsafe_allow_html=True)

else:
    st.write("Upload a pdf")
