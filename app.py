import streamlit as st
import os
import google.generativeai as genai
from PIL import Image

def setup_page():
    st.header("📸 Ask a MLLM questions about your picture.", anchor=False, divider="blue")
    st.sidebar.header("Options", divider='rainbow')
    hide_menu_style = """
            <style>
            #MainMenu {visibility: hidden;}
            </style>
            """
    st.markdown(hide_menu_style, unsafe_allow_html=True)
    

def main():
    """
    1. set up page
    2. ask user to take a picture
    3. submit to MLLM with a prompt
    4. display response

    Returns
    -------
    None.

    """
    
    setup_page()
    
    camera_image = st.camera_input("Take a picture")
    if camera_image:
        img = Image.open(camera_image)
        question = st.text_input("Enter your prompt/question and hit return","")
        if question:
            client = genai.GenerativeModel(model_name='gemini-1.0-pro-vision-latest')
            responses = client.generate_content([question, img],generation_config=genai.types.GenerationConfig
                                                (temperature=0.2, max_output_tokens=300))
            responses.resolve()
            st.markdown(responses.text)
             
    
if __name__ == '__main__':
    GOOGLE_API_KEY = os.environ.get('GOOGLE_API_KEY_NEW')
    genai.configure(api_key=GOOGLE_API_KEY)
    main()
