from config.conf import AUD_FILE_PATH, MODEL_NAME, API_KEY
from utilities.audio_text import run_model
from utilities.text_summariser import sentence_summariser, initialise_model

print ("Entry Handler started...")
contents = run_model(AUD_FILE_PATH)
print (contents)
print("Audio to text completed")
# res = read_file(FILE_PATH)
initialise_model(API_KEY)
sentence_summariser(contents, MODEL_NAME)
print ("Text summarised successfully")

