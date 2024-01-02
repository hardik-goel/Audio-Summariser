from config.conf import AUD_FILE_PATH, API_KEY, MODEL_NAME
from utilities.audio_text import run_model
from utilities.text_summariser import sentence_summariser, initialise_model
import warnings

# Suppress the specific warning
warnings.filterwarnings("ignore", message="FP16 is not supported on CPU; using FP32 instead")
print ("Entry Handler started...")
contents = run_model(AUD_FILE_PATH)
print (contents)
print("Audio to text completed")
# res = read_file(FILE_PATH)
model = initialise_model(API_KEY,MODEL_NAME)
summary = sentence_summariser(contents,model)
print ("Text summarised successfully")

