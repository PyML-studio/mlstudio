import os
import requests
import streamlit as st
from streamlit_lottie import st_lottie

import recorder
import openai

# constants
LOTTIE_URL = 'https://assets6.lottiefiles.com/packages/lf20_6e0qqtpa.json'
PROMPT_WAVFILE = 'prompt.wav'

# setup tjhe API
home_dir = os.path.expanduser("~")
openai.api_key_path = os.path.join(home_dir, 'OPENAI_API_KEY')

# Create the animation
def load_lottieur(url):
    r = requests.get(url)
    if r.status_code != 200:
        return
    return r.json()

lottie_anim = load_lottieur(LOTTIE_URL)

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

    # record the prompt
    recorder.record(filename=PROMPT_WAVFILE)

    # Process recording
    audio_file = open(PROMPT_WAVFILE, 'rb')
    transcript = openai.Audio.translate("whisper-1", audio_file)
    #import json
    #json.dump(transcript, open('transcript.json', 'wt'))
    #transcript = json.load(open('transcript.json', 'rt'))

    st.session_state.is_recording = False
    st.session_state.prompt_text = transcript
    st.session_state.chat_text = transcript



##########################
with st.container():
    left, right = st.columns([2, 3])
    with left:
        st_lottie(lottie_anim, height=300, key='coding')

    with right:
        st.subheader('Hi, I am ChatGPT voice :audio: assistant!')

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

    chat_box = st.empty()
    if st.session_state.chat_text:
        chat_box.write(st.session_state.chat_text)


