import google.generativeai as genai


# def read_file(FILE_PATH):
#     with open(FILE_PATH, "r") as f:
#         res = f.read()
#         f.close()
#     print("File Read successfully")
#     return res

def initialise_model(API_KEY,MODEL_NAME):
    genai.configure(api_key=API_KEY)
    model = genai.GenerativeModel(MODEL_NAME)
    return model



def sentence_summariser(CONTENT, MODEL):
    print("\nStarting Sentence Summary\n")
    text_prompt = CONTENT + "\n Summarise this text."
    responses = MODEL.generate_content(text_prompt)
    responses.prompt_feedback  # To validate whether it complies with safety norms
    for response in responses:
        summary = response.text
        print(summary, end="")
    return summary

    # TODO
    # Test end to end with more audios.
