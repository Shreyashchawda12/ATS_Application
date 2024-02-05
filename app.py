import os
import streamlit as st
import io
import base64
import pdf2image
from PIL import Image
import google.generativeai as genai


from dotenv import load_dotenv

load_dotenv()


genai.configure(api_key=os.getenv('GOOGLE_API_KEY'))

def get_gemini_response(input,pdf_content,prompt):
    model = genai.GenerativeModel('gemini-pro-vision')
    response = model.generate_content([input,pdf_content[0],prompt])
    return response.text

def input_pdf_setup(uploaded_file):
    if uploaded_file is not None:
        ## Convert the PDF to image
        images=pdf2image.convert_from_bytes(uploaded_file.read())

        first_page=images[0]

        # Convert to bytes
        img_byte_arr = io.BytesIO()
        first_page.save(img_byte_arr, format='JPEG')
        img_byte_arr = img_byte_arr.getvalue()

        pdf_parts = [
            {
                "mime_type": "image/jpeg",
                "data": base64.b64encode(img_byte_arr).decode()  # encode to base64
            }
        ]
        return pdf_parts
    else:
        raise FileNotFoundError("No file uploaded")

    
st.set_page_config(page_title="ATS Resume Assistant")
st.header("ATS Application")
input_text = st.text_area("Job Description: ",key="input")
uploaded_file = st.file_uploader("upload your resume(PDF)...",type=["PDF"])

if uploaded_file is not None:
    st.write("PDF Uploaded Successfully")
    
submit1 = st.button("Tell me about the reume")

submit2 = st.button("Percentage Match")

input_prompt1 = """
You are the experience HR with Tech Experience in the field of any one job role from Data science, Data Analyst, Data Engineer, Big Data Engineer,
NLP Engineer, Python Developer etc. Your task is to review the provided resume against the Job Description for these profile.
Please share your professional evaluation on whether the candidate's profile align with this Job Description. Highlisht strengths
and weaknesses of the applicant in relation to the specific job role.
""" 

input_prompt2 = """
You are skilled ATS (Application Tracking System) scanner with a deep understanding of the Data science or Data Analyst or Data Engineer or Big Data Engineer or
NLP Engineer or Python Developer. Your task is to evaluate the resume against provided Job Description. Give me the percentage match
based on the job description. First output should come as the percentage and then keyword missing and last final thought.
"""   

if submit1:
    if uploaded_file is not None:
        pdf_content = input_pdf_setup(uploaded_file)
        response = get_gemini_response(input_prompt1, pdf_content,input_text)
        st.subheader("The response is")
        st.write(response)
    else:
        st.write("Please upload resume")
        
elif submit2:
    if uploaded_file is not None:
        pdf_content = input_pdf_setup(uploaded_file)
        response = get_gemini_response(input_prompt2, pdf_content,input_text)
        st.subheader("The response is")
        st.write(response)
    else:
        st.write("Please upload resume")
    