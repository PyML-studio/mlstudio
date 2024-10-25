import os
import tempfile
from io import BytesIO
from gtts import gTTS
from playsound import playsound


def run_tts(text):
    tts = gTTS(text)
    mp3_fp = BytesIO()
    tts.write_to_fp(mp3_fp)

    # Extract the byte string from the BytesIO object
    mp3_bytes = mp3_fp.getvalue()

    # Save the audio data to a temporary file
    with tempfile.NamedTemporaryFile(suffix='.mp3', delete=False) as f:
        f.write(mp3_bytes)
        audio_file = f.name
        temp_file_path = f.name
        print('temp_file_path:', temp_file_path)

    # Play the audio data using the playsound module
    playsound(audio_file)

    # Delete the temporary audio file
    # os.unlink(audio_file)

if __name__ == '__main__':
    run_tts(text='this is a test')