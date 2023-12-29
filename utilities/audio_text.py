import whisper
from transformers import pipeline

model = whisper.load_model("base")
res = model.transcribe("resources/sample_order_recording.wav")
# res = model.transcribe("/Users/hardikgoel/Downloads/trials/sentence_summary/sample_order_recording.wav")
result = res["text"]
print(result)
