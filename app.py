import streamlit as st
import PyPDF2
import docx
import google.generativeai as genai

# --- CONFIGURATION ---
try:
    API_KEY = "AIzaSyAReJQucVhjChnpgJxO1VykU2RsajR_btw"  # Use st.secrets for deployment
    genai.configure(api_key=API_KEY)
except Exception as e:
    st.error(f"Failed to configure Gemini: {e}")

# --- HELPER FUNCTIONS ---
def extract_text_from_pdf(file_obj):
    # ... (your function, but it takes a file object) ...
    pass

def extract_text_from_docx(file_obj):
    # ... (your function, but it takes a file object) ...
    pass

def get_ai_feedback(resume_text):
    # ... (your function) ...
    model = genai.GenerativeModel(model_name='gemini-2.5-flash')
    response = model.generate_content(resume_text)
    return response.text

# --- STREAMLIT APP LAYOUT ---
st.set_page_config(layout="wide")
st.title("ResumeMentor 💼🔥")

uploaded_file = st.file_uploader("Upload your resume (PDF or DOCX)", type=["pdf", "docx"])

if uploaded_file is not None:
    # Display the user's "message"
    with st.chat_message("user"):
        st.write(f"Uploaded: {uploaded_file.name}")

    # Process the file
    resume_text = ""
    with st.spinner("Analyzing resume..."):
        try:
            if uploaded_file.name.lower().endswith('.pdf'):
                resume_text = extract_text_from_pdf(uploaded_file)
            elif uploaded_file.name.lower().endswith('.docx'):
                resume_text = extract_text_from_docx(uploaded_file)
            
            if resume_text:
                feedback = get_ai_feedback(resume_text)
                # Display the AI's response
                with st.chat_message("assistant"):
                    st.markdown(feedback)
            else:
                st.error("Could not extract text from the file.")
        except Exception as e:
            st.error(f"An error occurred: {e}")