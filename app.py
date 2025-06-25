from dotenv import load_dotenv

load_dotenv()
import base64
import streamlit as st
import os
import io
import fitz
from PIL import Image 
import google.generativeai as genai

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def get_gemini_response(input_prompt, resume_text, input_text):
    model = genai.GenerativeModel('gemini-1.5-flash')
    response = model.generate_content([input_prompt, resume_text, input_text])
    return response.text

def input_pdf_setup(uploaded_file):
    if uploaded_file is not None:
        doc = fitz.open(stream=uploaded_file.read(), filetype="pdf")
        full_text = ""
        for page in doc:
            full_text += page.get_text()
        return full_text
    else:
        raise FileNotFoundError("No file uploaded")

## Streamlit App

st.set_page_config(page_title="AI-powered Resume Matching")
st.header("Hire Match AI")
input_text=st.text_area("Job Description: ",key="input")
uploaded_file=st.file_uploader("Upload your resume(PDF)",type=["pdf"])


if uploaded_file is not None:
    st.write("PDF Uploaded Successfully")


submit1 = st.button("Tell Me About the Resume")

#submit2 = st.button("How Can I Improvise my Skills")

submit3 = st.button("Percentage match")

submit4 = st.button("Create Cover letter")

input_prompt1 = """
    You are an experienced Technical Human Resource Manager,your task is to review the provided resume against the job description. 
    Please share your professional evaluation on whether the candidate's profile aligns with the role. 
    Highlight the strengths and weaknesses of the applicant in relation to the specified job requirements.
"""

input_prompt2 = """
You are an skilled ATS (Applicant Tracking System) scanner with a deep understanding of data science and ATS functionality, 
your task is to evaluate the resume against the provided job description. give me the percentage of match if the resume matches
the job description. First the output should come as percentage and then keywords missing and last final thoughts.
"""

input_prompt3 = """
You are a highly skilled ATS (Applicant Tracking System) evaluator with deep expertise in resume parsing and ATS keyword algorithms.

Your task is to:
1. Analyze the provided resume and job description.
2. Calculate the match percentage between the resume and the job description based on keyword alignment, skill relevance, and role fit.
3. Extract and list all important keywords or phrases from the job description.
4. Identify important keywords or phrases that are missing in the resume but appear in the job description.
5. Provide final thoughts on how the resume could be improved to better match the job description.

Output format:
1. Match Percentage: XX%
2. Extracted Keywords and Phrases: [list bullet points]
3. Missing Keywords: [list of keywords in bullet points]
4. Final Thoughts: [short paragraph with recommendations]

Be objective and use clear language. Your assessment will help optimize the resume for applicant tracking systems.
"""

input_prompt4 = """
You are a professional cover letter writer with deep knowledge of hiring practices and ATS optimization.
Your task is to:
1. Read the provided resume and job description.
2. Write a compelling, tailored cover letter that highlights the candidate’s qualifications, experience, and alignment with the job requirements.
3. Use a confident, professional tone while maintaining clarity and conciseness.
4. The letter should include:
    - A strong opening that shows interest in the company and role.
    - A middle section that aligns the candidate’s experience with the job requirements.
    - A closing paragraph that expresses enthusiasm and invites further discussion.
5. Keep the cover letter within 300 words.
"""

if submit1:
    if uploaded_file is not None:
        pdf_content=input_pdf_setup(uploaded_file)
        response=get_gemini_response(input_prompt1,pdf_content,input_text)
        st.subheader("The Response is")
        st.write(response)
    else:
        st.write("Please upload the resume")

elif submit3:
    if uploaded_file is not None:
        pdf_content=input_pdf_setup(uploaded_file)
        response=get_gemini_response(input_prompt3,pdf_content,input_text)
        st.subheader("The Response is")
        st.code(response, language='markdown')
    else:
        st.write("Please upload the resume")

elif submit4:
    if uploaded_file is not None:
        pdf_content=input_pdf_setup(uploaded_file)
        response=get_gemini_response(input_prompt4,pdf_content,input_text)
        st.subheader("The Response is")
        st.write(response)
    else:
        st.write("Please upload the resume")
