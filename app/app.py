import io
import os
import shutil
import sys
import tempfile

import streamlit as st
import torch

CONTENT_ROOT_PATH = '/Users/hardikgoel/Downloads/github/AudioSummariser'
sys.path.append(CONTENT_ROOT_PATH)
from main.entry_handler import aud_text
from pydub import AudioSegment
import numpy as np


def copy_uploaded_audio(uploaded_file):
    if uploaded_file is not None:
        try:
            resources_path = os.path.join(CONTENT_ROOT_PATH, "resources")
            # Create a temporary file in the resources directory
            temp_file = tempfile.NamedTemporaryFile(delete=False, dir=resources_path, suffix=".wav")
            temp_file_path = temp_file.name

            # Copy the contents of the uploaded file to the temporary file
            shutil.copyfileobj(uploaded_file, temp_file)

            # Close the temporary file
            temp_file.close()

            # Return the path of the saved temporary file
            return temp_file_path
        except Exception as e:
            print(f"Error copying uploaded audio: {e}")
            return None

def main():
    st.title("Audio Summarisation App")

    uploaded_file = st.file_uploader("Choose an audio file", type=["wav", "mp3"])
    resources_path = os.path.join(CONTENT_ROOT_PATH, "resources")
    # uploaded_file = "/Users/hardikgoel/Downloads/github/AudioSummariser/resources/sample_order_recording.wav"
    # resource_path = f"{CONTENT_ROOT_PATH}/{resources}"
    if uploaded_file is not None:
        st.audio(uploaded_file, format="audio/wav", start_time=0)
        copied_audio_path = copy_uploaded_audio(uploaded_file)
        print(f"copied_audio_path::{copied_audio_path}")
        # print (f"uploaded_file::{uploaded_file}")

        #trying to write audio content, but gives decoding error.
        # audio_content = uploaded_file.read()
        #
        # output_file_path = f"{CONTENT_ROOT_PATH}/resources/temp.wav"
        # print(f"output_file_path::{output_file_path}")
        # with open(output_file_path, "wb") as output_file:
        #     output_file.write(audio_content)

        # Get the full path of the uploaded file
        # file_path = os.path.join(CONTENT_ROOT_PATH, uploaded_file.name)
        # print (f"Content of the audio file:\n{audio_content}")
        # Convert the audio content to a NumPy array as streamlit returns an uploadedFile object

        audio_np = preprocess_audio(uploaded_file)
        # Add a "Convert" button
        if st.button("Convert"):
            if audio_np is not None:
                # Run the model and display the result
                #audio_np is giving tensor values
                # print(f"file_path::{copied_audio_path}")
                #Leaving it here as not sure from where would be getting the path which would be supplied here
                result = aud_text(copied_audio_path)
                st.subheader("Transcription Result:")
                st.text(result)
            else:
                st.warning("Please upload an audio file before converting.")

def preprocess_audio(uploaded_file):
    if uploaded_file is not None:
        try:
            # Read the contents of the uploaded file
            audio_content = io.BytesIO(uploaded_file.read())

            # Convert the audio content to a Pydub AudioSegment
            audio_segment = AudioSegment.from_file(audio_content, format=uploaded_file.type)

            # Convert Pydub AudioSegment to NumPy array
            audio_np = np.array(audio_segment.get_array_of_samples())

            # Convert NumPy array integer values to torch.FloatTensor
            audio_tensor = torch.FloatTensor(audio_np)

            return audio_tensor
        except Exception as e:
            print(f"Error preprocessing audio: {e}")
            return None
    else:
        return None



if __name__ == "__main__":
    main()

#The command to run :
# streamlit run app.py
