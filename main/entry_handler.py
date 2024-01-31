from config.conf import API_KEY, MODEL_NAME, IMAGE_PATH
from utilities.audio_text import run_model
from utilities.chart_creation import graph_formation
from utilities.file_reads import fetch_audio_files
from utilities.sentiment_analyser import analyze_sentiment, display_word_sentiment
from utilities.text_summariser import sentence_summariser, initialise_model, generate_code_from_img
import warnings

# Suppress the specific warning
warnings.filterwarnings("ignore", message="FP16 is not supported on CPU; using FP32 instead")
# print ("Fetching audio files...")
# AUD_FILE_PATH = fetch_audio_files()
# print ("Entry Handler started...")
# contents = run_model(AUD_FILE_PATH)
# print (contents)
# print("Audio to text completed")
# # res = read_file(FILE_PATH)
model = initialise_model(API_KEY,MODEL_NAME)
# summary = sentence_summariser(contents,model)
# print ("\nText summarised successfully")
# print ("Sentiment analysis started")
# sentiment = analyze_sentiment(summary)
# print ("\nSentiment analysis completed")
# print ("\nWord Sentiment started")
# words, counts, sentiments = display_word_sentiment(summary)
# print ("\nGraph formation started")
# graph_formation(words, counts, sentiments)
# print ("\nWordClouds and top 5 words with their sentiment completed successfully")
generate_code_from_img(IMAGE_PATH, model)


