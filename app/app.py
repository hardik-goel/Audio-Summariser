import streamlit as st
import sys
import os
from googleapiclient.discovery import build
from google.oauth2 import service_account
import torch

# Add the absolute path of the parent directory to the Python path
from googleapiclient.errors import HttpError
from googleapiclient.http import MediaFileUpload
from streamlit.elements import media

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from main.entry_handler import aud_text, sentiment_calculate
from pydub import AudioSegment
import numpy as np
from config.conf import MODEL_NAME, GOOGLE_DRIVE_KEY_PATH, google_drive_folder_id

# Set up Google Drive API credentials
credentials = service_account.Credentials.from_service_account_file(GOOGLE_DRIVE_KEY_PATH)
drive_service = build('drive', 'v3', credentials=credentials)


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


def upload_to_google_drive(uploaded_file):
    try:
        if uploaded_file is not None:
            # Save the uploaded file to a temporary location
            temp_file_path = f'/tmp/{uploaded_file.name}'
            uploaded_file.seek(0)
            with open(temp_file_path, 'wb') as temp_file:
                temp_file.write(uploaded_file.read())

            file_metadata = {
                'name': uploaded_file.name,
                'parents': [google_drive_folder_id]
            }

            # Use the temporary file path when creating MediaFileUpload
            media = MediaFileUpload(temp_file_path, mimetype=uploaded_file.type)

            created_file = drive_service.files().create(
                body=file_metadata,
                media_body=media,
                fields='id'
            ).execute()
            st.success('File uploaded successfully!')
            file_path = f"https://drive.google.com/file/d/{created_file['id']}"
            st.write('File Path:', file_path)

            # Remove the temporary file after uploading
            os.remove(temp_file_path)

            return file_path

    except HttpError as e:
        st.error(f"An error occurred: {e}")
        return None


def main():
    st.title("Audio Summarisation App")

    uploaded_file = st.file_uploader("Choose an audio file", type=["wav", "mp3"])

    if uploaded_file is not None:
        # Display the uploaded audio file
        st.audio(uploaded_file, format="audio/wav", start_time=0)

        file_path = upload_to_google_drive(uploaded_file)

        # Get the file ID from the uploaded file
        file_id = file_path.split("/")[-1]

        # Get information about the uploaded file
        file_metadata = drive_service.files().get(fileId=file_id, fields='owners').execute()

        # Convert the audio content to a NumPy array as streamlit returns an uploadedFile object
        # not sure if this is needed
        # audio_np = preprocess_audio(uploaded_file)

        # Run the model and display the result
        result = aud_text(file_path)
        st.subheader("Transcription Result:")
        st.text(result)
        sentiment_calculate(result, MODEL_NAME)


if __name__ == "__main__":
    main()
