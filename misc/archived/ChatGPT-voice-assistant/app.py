import os
import requests
import json

import streamlit as st
from streamlit_lottie import st_lottie

# local modules
import audio_recorder
import audio_text2speech
import openai_whisper
import openai_chatgpt

# constants
LOTTIE_URL = 'https://assets6.lottiefiles.com/packages/lf20_6e0qqtpa.json'
PROMPT_WAVFILE = 'prompt.wav'


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

    # record the prompt
    audio_recorder.record(filename=PROMPT_WAVFILE)
    prompt_box.write("Processing the prompt ...")

    # Process recording
    prompt = openai_whisper.get_transcription(PROMPT_WAVFILE)
    #import json
    #json.dump(transcript, open('transcript.json', 'wt'))
    #transcript = json.load(open('transcript.json', 'rt'))

    st.session_state.is_recording = False
    st.session_state.prompt_text = prompt

    response = openai_chatgpt.get_response(prompt)
    json.dump(response, open('response.json', 'wt'))

    st.session_state.chat_text = response


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
            audio_text2speech.run_tts(line)

        # write the entire message
        message_box.write(choice['message']['content'])