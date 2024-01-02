# # from vertexai.preview.generative_models import (
# #     GenerationConfig,
# #     GenerativeModel,
# #     Image,
# #     Part,
# # )
# #
# FILE_PATH = "/Users/hardikgoel/Downloads/trials/sentence_summary/new/sample_text_orders.txt"
# # model = GenerativeModel("gemini-pro")
# #
# text_prompt = FILE_PATH+"\n Summarise this text."
# # responses = model.generate_content(text_prompt, stream=True)
# #
# # for response in responses:
# #     print(response.text, end="")
#
# import vertexai
# from vertexai.preview.generative_models import GenerativeModel
#
#
# def generate_text(project_id: str, location: str) -> str:
#     # Initialize Vertex AI
#     vertexai.init(project=project_id, location=location)
#     # Load the model
#     multimodal_model = GenerativeModel("gemini-pro")
#     # Query the model
#     response = multimodal_model.generate_content(
#         [text_prompt]
#     )
#     print(response)
#     return response.text
#
# generate_text()
#
#
#
# from cryptography.fernet import Fernet
#
# def initialise_model(API_KEY):
#     genai.configure(api_key=API_KEY)
#     model = genai.GenerativeModel()
#     return model
#
# CONTENT = "Thank you for calling Martha's Flores,Thomas Sissy. Hello, I'd like to order flowers and I think you have what I'm looking for.I'd be happy to take care of your order. May I have your name please?Randall Thomas. Randall Thomas, can you spell that for me? Randall, ANBAL, Thomas, THO, and AS.Thank you for that information Randall. May I have your home or office number area code first?That's 409-866-5088. That's 409-866-5088. Do you have a fax number or email address?Randall. they are Randall Thomas at www.chimell.com may have your shipping addresses.Cats and children stroll forward for seihzu told 77-706 With products translated to employment,thank you for your information, interested in purchasing. Red roses, probably a dozen.One dozen of red roses do you want long stems? They are sure. All right, Randall, let me process your order.One moment please. Okay. Randall, you are ordering one dozen long-stained red roses.The total amount of your order is $40 and it will be shipped to your address within 24 hours.I was thinking to deliver my roses within 24 hours. Okay, no problem. Is your answer out?I can help you with? That's all for now, thing. No problem, Randall.Thank you for calling Martha's Flores. Have a nice day."
# def summarise(model,)
# text_prompt = CONTENT+"\n Summarise this text."
# responses = model.generate_content(text_prompt)
# responses.prompt_feedback  #To validate whether it complies with safety norms
#
# for response in responses:
#     print(response.text, end="")
#
