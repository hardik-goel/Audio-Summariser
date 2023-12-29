from transformers import pipeline, BartTokenizer

# file_path = "resources/sample_text_limitation.txt"
# file_path = "resources/sample_text_orders.txt"
#file_path = "/Users/hardikgoel/Downloads/trials/sentence_summary/new/sample_text_limitation.txt"
file_path = "/Users/hardikgoel/Downloads/trials/sentence_summary/new/sample_text_orders.txt"
with open(file_path, "r") as f:
    res = f.read()
print("\nStarting Sentence Summary\n")
print(f"Length of the audio original string is {len(res)}")
result = f"Summarise the following text in less than {len(res)/2} words." + res
# f"Remove the noise and mention the facts correctly and clearly.\n{res}"
print (f"\nLimiting the summariser to {round(len(res)/2)} words from accuracy perspective\n")
# summarizer = pipeline("summarization", model="facebook/bart-base")
tokenizer = BartTokenizer.from_pretrained("facebook/bart-large-cnn")
tokens = tokenizer.tokenize(res)

#LIMITATION RIGHT NOW
#TODO

# Check if the number of tokens is more than the maximum limit
# if len(tokens) > 1024:
#     # If so, truncate the tokens to the maximum limit
#     tokens = tokens[:1024]
# # Convert tokens to string
# truncated_res = tokenizer.convert_tokens_to_string(tokens)

input_length = len(tokens)
print(f"Input length: {input_length}")  #for max length (token length)
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
summary = summarizer(result, max_length=input_length, min_length=0)[0]["summary_text"]
print(summary)
print("\nSentence Summary Ended")

#TODO
#Test end to end with more audios.
