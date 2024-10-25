import os
import openai

# setup the API key
home_dir = os.path.expanduser("~")
openai.api_key_path = os.path.join(home_dir, 'OPENAI_API_KEY')


def get_transcription(filename):
    with open(filename, 'rb') as fp:
        transcript = openai.Audio.translate("whisper-1", fp)
    return transcript['text']