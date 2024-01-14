import matplotlib.pyplot as plt

# Assuming 'word', 'count', and 'sentiment_for_word' are lists obtained from display_word_sentiment function

def graph_formation(words, counts, sentiments):
    import matplotlib.pyplot as plt

    # Assuming 'words', 'counts', and 'sentiments' are lists obtained from display_word_sentiment function

    # Plot word count bar chart
    plt.figure(figsize=(10, 5))
    plt.bar(words, counts, color='blue')
    plt.xlabel('Words')
    plt.ylabel('Count')
    plt.title('Word Count Distribution')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.show()

    # Plot sentiment distribution pie chart
    sentiment_labels = list(set(sentiments))
    sentiment_counts = [sentiments.count(label) for label in sentiment_labels]

    plt.figure(figsize=(8, 8))
    plt.pie(sentiment_counts, labels=sentiment_labels, autopct='%1.1f%%', startangle=140,
            colors=['green', 'yellow', 'red'])
    plt.title('Sentiment Distribution')
    plt.show()

