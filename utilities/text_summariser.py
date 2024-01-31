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
    print("\nStarting Sentence Summary")
    text_prompt = CONTENT + "\n Summarise this text."
    responses = MODEL.generate_content(text_prompt)
    responses.prompt_feedback  # To validate whether it complies with safety norms
    for response in responses:
        summary = response.text
        print(summary, end="")
    return summary

def generate_code_from_img(IMAGE, MODEL):
    print("\nStarting Code Generation\n\n")
    text_prompt = IMAGE + "\n Generate HTML, CSS code from this image page."
    responses = MODEL.generate_content(text_prompt)
    for response in responses:
        code = response.text
        print(code, end="")
    with open("image.html", "w") as f:
        f.write(code)
    # validate_code_to_image(code, MODEL)
    return code

# def validate_code_to_image(code, MODEL):
#     img = f"\n\nGenerate image from this code:: \n {code}"
#     img = PIL.Image.open('image.jpg')


