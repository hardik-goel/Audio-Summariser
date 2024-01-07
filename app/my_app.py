import sys

CONTENT_ROOT_PATH = '/Users/hardikgoel/Downloads/github/AudioSummariser'
sys.path.append(CONTENT_ROOT_PATH)

import my_app as gr
import torch
from main.entry_handler import aud_text
from pydub import AudioSegment
import numpy as np

# Function to preprocess audio
def preprocess_audio(uploaded_file):
    if uploaded_file is not None:
        audio_content = AudioSegment.from_file(uploaded_file)
        audio_np = np.array(audio_content.get_array_of_samples())
        audio_tensor = torch.FloatTensor(audio_np)
        return audio_tensor
    else:
        return None

# Gradio interface
def transcribe_audio(file):
    gr.audio(file, format="audio/wav", start_time=0)
    audio_np = preprocess_audio(file)
    if audio_np is not None:
        result = aud_text(file.name)
        return result
    else:
        return "Please upload a valid audio file."

iface = gr.Interface(
    fn=transcribe_audio,
    inputs=gr.File(type="audio", label="Upload Audio File (WAV)"),
    outputs="text",
    live=True,
    interpretation="default"
)

iface.launch(share=True)
