import glob
import os
from config.conf import AUD_FILE_PATH

file_paths = glob.glob(os.path.join(AUD_FILE_PATH, '*'))

def fetch_audio_files():
    for file_path in file_paths:
        filename = os.path.basename(file_path)
        print(f"Processing file: {filename}")
    return file_path
