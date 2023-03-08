import time
import streamlit as st


st.header('Hi, I am ChatGPT voice assistant!')

# Initialize session state
if "is_recording" not in st.session_state:
    st.session_state.is_recording = False

# Define button callbacks
def callback_record():
    st.session_state.is_recording = True
    messages_box.write("Recording started.")
    #st.experimental_rerun()

def callback_stop():
    st.session_state.is_recording = False
    messages_box.write("Recording stopped.")
    time.sleep(5)
    #st.experimental_rerun()

# Create two columns for buttons
col1, col2 = st.columns(2)

# Render buttons based on recording state
col1_button = col1.button(
    label="Record", type='primary', on_click=callback_record,
    disabled=st.session_state.is_recording)
col2_button = col2.button(
    label="Stop recording", type='primary', on_click=callback_stop,
    disabled=not st.session_state.is_recording)


# Initialize system messages box
messages_box = st.empty()
