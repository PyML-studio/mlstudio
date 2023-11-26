import pyaudio
import wave

# Set audio parameters
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 16000  # 44100
CHUNK = 1024
RECORD_SECONDS = 5
RECORDING_FILENAME = 'recording.wav'


def record(seconds=RECORD_SECONDS, filename=RECORDING_FILENAME):
    # Initialize PyAudio object
    audio = pyaudio.PyAudio()

    # Open audio stream
    stream = audio.open(
        format=FORMAT, channels=CHANNELS,
        rate=RATE, input=True,
        frames_per_buffer=CHUNK)
        
    # Record audio
    frames = []
    for i in range(0, int(RATE / CHUNK * seconds)):
        data = stream.read(CHUNK)
        frames.append(data)

    # Stop audio stream and PyAudio object
    stream.stop_stream()
    stream.close()
    audio.terminate()

    # Write frames to a WAV file
    wave_file = wave.open(filename, 'wb')
    wave_file.setnchannels(CHANNELS)
    wave_file.setsampwidth(audio.get_sample_size(FORMAT))
    wave_file.setframerate(RATE)
    wave_file.writeframes(b''.join(frames))
    wave_file.close()

if __name__ == '__main__':
    record()