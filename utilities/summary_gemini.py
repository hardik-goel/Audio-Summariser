# from vertexai.preview.generative_models import (
#     GenerationConfig,
#     GenerativeModel,
#     Image,
#     Part,
# )
#
FILE_PATH = "/Users/hardikgoel/Downloads/trials/sentence_summary/new/sample_text_orders.txt"
# model = GenerativeModel("gemini-pro")
#
text_prompt = FILE_PATH+"\n Summarise this text."
# responses = model.generate_content(text_prompt, stream=True)
#
# for response in responses:
#     print(response.text, end="")

import vertexai
from vertexai.preview.generative_models import GenerativeModel


def generate_text(project_id: str, location: str) -> str:
    # Initialize Vertex AI
    vertexai.init(project=project_id, location=location)
    # Load the model
    multimodal_model = GenerativeModel("gemini-pro")
    # Query the model
    response = multimodal_model.generate_content(
        [text_prompt]
    )
    print(response)
    return response.text

generate_text()
