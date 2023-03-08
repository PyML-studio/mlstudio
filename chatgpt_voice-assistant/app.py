import requests
import streamlit as st
from streamlit_lottie import st_lottie

import recorder


LOTTIE_URL = 'https://assets6.lottiefiles.com/packages/lf20_6e0qqtpa.json'
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
if "recording_is_done" not in st.session_state:
    st.session_state.recording_is_done = False


# Define button callbacks
def callback_record():
    st.session_state.is_recording = True
    prompt_box.write("Recording started.")

    recorder.record(filename='prompt.wav')


##########################
with st.container():
    left, right = st.columns(2)
    with left:
        st_lottie(lottie_anim, height=300, key='coding')

    with right:
        st.subheader('Hi, I am ChatGPT voice assistant!')

        st.write(':microphone: Press Record to start recording your promot')

        col1_button = st.button(
            label="Record :microphone:", type='primary',
            on_click=callback_record,
            disabled=st.session_state.is_recording)

        prompt_box = st.empty()


##########################
with st.container():
    st.write('---')
    messages_box = st.empty()

