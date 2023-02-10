# -*- coding: utf-8 -*-

import datetime
import streamlit as st  #Web App
import requests
import os
# import basic
import basic_OCR
import aspose.words as aw

'''
Uploading file in the form of pdf, doc and docx format 
'''

st.title("INVOICE PARSER")
input_file=st.file_uploader(label='UPLOAD PDF FILE HERE:',type=['pdf','doc','docx'])

'''
Checking uploaded file is pdf or doc or docx
'''
if input_file is not None:
    if input_file.type == "application/pdf":
        with open(os.path.join("uploaded_files", input_file.name),"wb") as f:
                f.write((input_file).getbuffer())
        pdf_file = os.path.join("./uploaded_files/", input_file.name)
        basic_OCR.result_data(pdf_file)
        st.success("Invoice Data Extracted Successfully")
        
    else:
        doc = aw.Document(input_file)
        doc.save("./uploaded_files/temp.pdf")
        basic_OCR.result_data('./uploaded_files/temp.pdf')

else:
    st.write("Upload a pdf")
