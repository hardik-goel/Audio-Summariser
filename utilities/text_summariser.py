from transformers import pipeline, BartTokenizer

# def read_file(FILE_PATH):
#     with open(FILE_PATH, "r") as f:
#         res = f.read()
#         f.close()
#     print("File Read successfully")
#     return res

def sentence_summariser(res, MODEL_NAME):
    print("\nStarting Sentence Summary\n")
    # print(f"Length of the audio original string is {len(res)}")
    result = f"Summarise the following text in less than {round(len(res)/2)} words." + res
    # print (f"\nLimiting the summariser to {round(len(res)/2)} words from accuracy perspective\n")
    tokenizer = BartTokenizer.from_pretrained(MODEL_NAME)
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
    # print(f"Input length: {input_length}\n")  #for max length (token length)
    summarizer = pipeline("summarization", model=MODEL_NAME)
    summary = summarizer(result, max_length=input_length, min_length=0)[0]["summary_text"]
    print(summary)
    print("\nSentence Summary Ended")

    #TODO
    #Test end to end with more audios.
