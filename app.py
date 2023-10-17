import streamlit as st
from src import main, utils
import tempfile

st.title("Hi, I'm Your Job Application Assistant 🧑")
st.write(
    "Based on your CV and Job description, I can help with with the following:\n1. Draft you a custom Cover letter\n2. Advise on Job application related questions"
)

st.write("---")
# Common components
st.write("**1. Upload your PDF document.** 📃")
fileobj = st.file_uploader("Upload PDF", type=["pdf"])

st.write("---")
st.write("**2. Paste the Job description below.** 👇")
job_description = st.text_area(
    "Include the Role, Company name, and Job responsibilities for better results",
    height=200,
    placeholder="Job Description here",
).strip()

st.write("---")
# Application Consultation
st.write("**3. Application Consultation question** 🎙️")
task = st.text_input(
    "Enter your Application question here to get suggestions. e.g: Why should we hire you?",
    placeholder="Paste Question here",
).strip()
if st.button("Consult"):
    if utils.validate(fileobj, job_description, task):
        with tempfile.NamedTemporaryFile(suffix=".pdf", delete=True) as tmp_file:
            tmp_file.write(fileobj.getvalue())
            tmp_file_path = tmp_file.name

            utils.show_info("Generated Response:")
            with st.spinner(text="🤔 Let me think a bit ..."):
                main.consult_agent(tmp_file_path, task=task, job_desc=job_description)

st.write("---")
# Cover Letter
st.write("**4. Create you Cover Letter draft** ✉️")
if st.button("Generate"):
    if utils.validate(fileobj, job_description, task):
        with tempfile.NamedTemporaryFile(suffix=".pdf", delete=True) as tmp_file:
            tmp_file.write(fileobj.getvalue())
            tmp_file_path = tmp_file.name

            utils.show_info("Generated Cover Letter:")
            with st.spinner(text="✍🏻 Give me some time to craft your cover letter ..."):
                main.generate_cover_letter(tmp_file_path, job_description)
