from config.conf import AUD_FILE_PATH, MODEL_NAME
from utilities.audio_text import run_model
from utilities.text_summariser import read_file, sentence_summariser

print ("Entry Handler started...")
FILE_PATH = run_model(AUD_FILE_PATH)
print (FILE_PATH)
print("Audio to text completed")
res = read_file(FILE_PATH)
sentence_summariser(res, MODEL_NAME)

