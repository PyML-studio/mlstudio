import time
import requests

import streamlit as st
from streamlit_lottie import st_lottie

# constants
LOTTIE_URL = 'https://assets6.lottiefiles.com/packages/lf20_6e0qqtpa.json'


# Create the animation
def load_lottie(url):
    r = requests.get(url)
    if r.status_code != 200:
        return
    return r.json()

lottie_anim = load_lottie(LOTTIE_URL)

st.set_page_config(page_title="ChatGPT-VA", page_icon='', layout='centered')

# Initialize session state
if "is_recording" not in st.session_state:
    st.session_state.is_recording = False
if "prompt_text" not in st.session_state:
    st.session_state.prompt_text = None
if "chat_text" not in st.session_state:
    st.session_state.chat_text = None


# Define button callbacks
def callback_record():
    st.session_state.is_recording = True
    prompt_box.write("Recording started ...")
    time.sleep(1)  #TODO

    # Record the prompt
    prompt_box.write("Processing the prompt ...")
    time.sleep(1)  #TODO

    # Process recording
    pass  #TODO

    st.session_state.is_recording = False
    st.session_state.prompt_text = ''  #TODO

    # Get ChatGPT's response
    pass  # TODO
    st.session_state.chat_text = '' # TODO


##########################
with st.container():
    left, right = st.columns([2, 3])
    with left:
        st_lottie(lottie_anim, height=300, key='coding')

    with right:
        st.subheader('Hi, I am ChatGPT Voice Assistant!')

        st.write('Press Record to start recording your promot')

        rec_button = st.button(
            label="Record :microphone:", type='primary',
            on_click=callback_record,
            disabled=st.session_state.is_recording)

        prompt_box = st.empty()
        if st.session_state.prompt_text:
            prompt_box.write(f'Prompt: {st.session_state.prompt_text}')


##########################
with st.container():
    st.write('---')

    message_box = st.empty()
    if st.session_state.chat_text:
        choice = st.session_state.chat_text['choices'][0]
        # write and play line by line
        for line in choice['message']['content'].split('\n'):
            if not line:
                continue
            message_box.write(line)
            # Run Text-to-Speech
            pass  #TODO

        # write the entire message
        message_box.write(choice['message']['content'])