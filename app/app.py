import os
import sys

import streamlit as st
import torch

CONTENT_ROOT_PATH = '/Users/hardikgoel/Downloads/github/AudioSummariser'
sys.path.append(CONTENT_ROOT_PATH)
from main.entry_handler import aud_text
from pydub import AudioSegment
import numpy as np

def main():
    st.title("Audio Summarisation App")

    uploaded_file = st.file_uploader("Choose an audio file", type=["wav", "mp3"])
    # uploaded_file = "/Users/hardikgoel/Downloads/github/AudioSummariser/resources/sample_order_recording.wav"

    if uploaded_file is not None:
        st.audio(uploaded_file, format="audio/wav", start_time=0)
        print (f"uploaded_file::{uploaded_file}")

        # Get the full path of the uploaded file
        file_path = os.path.join(CONTENT_ROOT_PATH, uploaded_file.name)

        # Convert the audio content to a NumPy array as streamlit returns an uploadedFile object
        audio_np = preprocess_audio(uploaded_file)
        # Add a "Convert" button
        if st.button("Convert"):
            if audio_np is not None:
                # Run the model and display the result
                #audio_np is giving tensor values
                print(f"file_path::{file_path}")
                #Leaving it here as not sure from where would be getting the path which would be supplied here
                result = aud_text(file_path)
                st.subheader("Transcription Result:")
                st.text(result)
            else:
                st.warning("Please upload an audio file before converting.")

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



if __name__ == "__main__":
    main()

#The command to run :
# streamlit run app.py
