import streamlit as st
import time


RED_TEXT = '*<p style="color:red;">{}</p>*'
GREEN_TEXT = '*<p style="color:green;">{}</p>*'


def stream(response):
    with st.empty():
        full_text = ""
        for text in response:
            full_text += text
            time.sleep(0.005)
            st.write(full_text)
        st.write(full_text)


def show_error(txt):
    st.write(RED_TEXT.format(txt), unsafe_allow_html=True)
    return False


def show_info(txt):
    st.write(GREEN_TEXT.format(txt), unsafe_allow_html=True)
    return False


def validate(fileobj, job_description, task):
    if fileobj is None:
        return show_error("Please Upload your CV/Resume (PDF format)")
    elif not job_description:
        return show_error("Please fill in the Job Description")
    elif not task:
        return show_error("Please fill in the Application question")
    return True
