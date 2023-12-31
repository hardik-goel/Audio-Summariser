import whisper


def run_model(AUD_FILE_PATH):
    model = whisper.load_model("base")
    res = model.transcribe(AUD_FILE_PATH)
    result = res["text"]
    return result
