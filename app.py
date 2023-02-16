import streamlit as st
import easyocr
import numpy as np
import PIL
import cv2
from haystack import Document, Pipeline
from haystack.nodes import FARMReader
from pdf2image import convert_from_bytes
from PIL import ImageDraw,Image
from io import BytesIO


threshold = 0.6
threshold_high = 0.7
threshold_low = 0.5

def draw_boxes(image, bounds, color='yellow', width=2):
    draw = ImageDraw.Draw(image)
    for bound in bounds:
        p0, p1, p2, p3 = bound[0]
        draw.line([*p0, *p1, *p2, *p3, *p0], fill=color, width=width)
    return image

def get_answer(result):
    if result['answers'][0].score >= threshold_high and result['answers'][0].score <= 1:
        return result['answers'][0].answer
    else:
        return '-'

def extraction(file):
    easyreader = easyocr.Reader(['en'], gpu=False, detector=True)
    new_reader = FARMReader(model_name_or_path=r"my_model_new_63")
    images = convert_from_bytes(file.read())
    image = images[0]
    bounds = easyreader.readtext(np.array(image), min_size=0, slope_ths=0.2, ycenter_ths=0.5, height_ths=0.5, y_ths=0.3, low_text=0.5, text_threshold=0.7, width_ths=0.8, paragraph=True, decoder='beamsearch', beamWidth=10)
    draw_boxes(image, bounds)
    context = '\n'.join([b[1] for b in bounds])
    p = Pipeline()
    p.add_node(component=new_reader, name="reader", inputs=["Query"])
    queries = [
        "invoice number?",
        "invoice date?",
        "Seller name?",
        "Address?",
        "Seller Phone number?",
        "Seller email Id?",
        "Seller Tax/GST/VAT number?",
        "Buyer billing name?",
        "Buyer shipping address?",
        "Buyer phone number?",
        "Buyer email Id?",
        "Buyer Tax/GST/VAT number?",
        "Sales tax/GST percentage?",
        "Gross total?",
        "Net amount?",
        "Due date?"
    ]
    results = [p.run(query=q, documents=[Document(content=context)]) for q in queries]
    myData = {q: get_answer(r) for q, r in zip(queries, results)}

    col1, col2 = st.columns(2)
    with col1:
        st.subheader('Uploaded Invoice')
        st.image(image, caption='Uploaded PDF', use_column_width=True)

    with col2:
        st.subheader('Extracted Details')
        for k, v in myData.items():
            if v != "-":
                st.write(f'{k}: {v}')

    return bounds, image


#st.title('')
st.set_page_config(layout="wide")
image = Image.open(r'BPAI_logo.png')
st.image(image,width=200)
#st.title("INVOICE PARSING")
# Changed the title style
st.markdown("<h1 style='text-align:center; color:purple;'>INVOICE PARSING</h1>", unsafe_allow_html=True)
file = st.file_uploader("Upload a PDF file", type=['pdf'])
if file is not None:
    with st.spinner("Extracting Invoice Data..."):
        bounds, image = extraction(file)
