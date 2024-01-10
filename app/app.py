import streamlit as st
import sys
from googleapiclient.discovery import build
from google.oauth2 import service_account
import torch
from main.entry_handler import aud_text, sentiment_calculate
from pydub import AudioSegment
import numpy as np
from config.conf import MODEL_NAME, GOOGLE_DRIVE_KEY

CONTENT_ROOT_PATH = '/Users/hardikgoel/Downloads/github/AudioSummariser'
sys.path.append(CONTENT_ROOT_PATH)

# Set up Google Drive API credentials
credentials = service_account.Credentials.from_service_account_file(GOOGLE_DRIVE_KEY)
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
    if uploaded_file is not None:
        file_metadata = {
            'name': uploaded_file.name,
            'parents': ['your_google_drive_folder_id']
        }
        media = drive_service.files().create(
            body=file_metadata,
            media_body=uploaded_file,
            fields='id'
        ).execute()
        st.success('File uploaded successfully!')
        file_path = f"https://drive.google.com/file/d/{media['id']}"
        st.write('File Path:', file_path)
        return file_path


def main():
    st.title("Audio Summarisation App")

    uploaded_file = st.file_uploader("Choose an audio file", type=["wav", "mp3"])


    file_metadata = drive_service.files().get(fileId=GOOGLE_DRIVE_KEY, fields='owners').execute()

    # Get the email address of the owner
    owner_email = file_metadata['owners'][0]['emailAddress']
    print('Owner Email:', owner_email)

    if uploaded_file is not None:

        # Display the uploaded audio file
        st.audio(uploaded_file, format="audio/wav", start_time=0)

        file_path = upload_to_google_drive(uploaded_file)
        # Convert the audio content to a NumPy array as streamlit returns an uploadedFile object
        #not sure if this is needed
        # audio_np = preprocess_audio(uploaded_file)

        # Run the model and display the result
        result = aud_text(file_path)
        st.subheader("Transcription Result:")
        st.text(result)
        sentiment_calculate(result, MODEL_NAME)


if __name__ == "__main__":
    main()