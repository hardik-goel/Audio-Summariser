import streamlit as st
import sys

import torch

CONTENT_ROOT_PATH = '/Users/hardikgoel/Downloads/github/AudioSummariser'
sys.path.append(CONTENT_ROOT_PATH)
from main.entry_handler import aud_text
from pydub import AudioSegment
import numpy as np

def preprocess_audio(uploaded_file):
    if uploaded_file is not None:
        # Convert the audio file content to a NumPy array
        audio_content = AudioSegment.from_file(uploaded_file)
        audio_np = np.array(audio_content.get_array_of_samples())

        # Convert NumPy array integer values to torch.FloatTensor
        audio_tensor = torch.FloatTensor(audio_np)

        return audio_tensor
    else:
        return None

def main():
    st.title("Audio Summarisation App")

    uploaded_file = st.file_uploader("Choose an audio file", type=["wav", "mp3"])

    if uploaded_file is not None:
        st.audio(uploaded_file, format="audio/wav", start_time=0)

        # Convert the audio content to a NumPy array as streamlit returns an uploadedFile object
        audio_np = preprocess_audio(uploaded_file)

        # Run the model and display the result
        result = aud_text(audio_np)
        st.subheader("Transcription Result:")
        st.text(result)


if __name__ == "__main__":
    main()
