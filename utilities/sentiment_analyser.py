import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import string

nltk.download('vader_lexicon')
nltk.download('stopwords')
nltk.download('punkt')

def generate_wordcloud(summary):
    # Generate word cloud
    wordcloud = WordCloud(width=800, height=400, random_state=42, background_color='white').generate(summary)

    # Display the word cloud
    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    plt.show()


def preprocess_text(summary):
    # Remove stopwords
    stop_words = set(stopwords.words('english'))
    word_tokens = word_tokenize(summary)
    punctuation = set(string.punctuation)   # will fix punctuation and provide a cleaner result
    filtered_text = [word for word in word_tokens if word.lower() not in stop_words and word.lower() not in punctuation]
    preprocess_text = ' '.join(filtered_text)
    return preprocess_text


def analyze_sentiment(summary):
    # Initialize the VADER sentiment analyzer
    sia = SentimentIntensityAnalyzer()

    # Analyze sentiment and clean the text by removing stopwords
    sentiment_score = sia.polarity_scores(preprocess_text(summary))

    # Determine sentiment based on the compound score
    if sentiment_score['compound'] >= 0.05:
        sentiment = 'Positive'
    elif sentiment_score['compound'] <= -0.05:
        sentiment = 'Negative'
    else:
        sentiment = 'Neutral'
    print (f"The overall sentiment is : {sentiment}")
    return sentiment


def tokenisation_sentiment_analysis_wordwise(summary):
    preprocessed_text = preprocess_text(summary)
    generate_wordcloud(preprocessed_text)
    # Tokenize the cleaned text
    word_tokens = word_tokenize(preprocessed_text)

    # Analyze sentiment for each word
    word_sentiments = {word: analyze_sentiment(word) for word in word_tokens}
    return word_tokens, word_sentiments


def display_word_sentiment(summary):
    word_tokens, word_sentiments = tokenisation_sentiment_analysis_wordwise(summary)
    # Count occurrences of each word
    word_counts = {word: word_tokens.count(word) for word in set(word_tokens)}

    # Get the top 5 words based on descending order of occurrence
    top_words = sorted(word_counts.items(), key=lambda x: x[1], reverse=True)[:5]

    # Display the top 5 words with their sentiment
    print("\nTop words along with Sentiment:")
    for word, count in top_words:
        sentiment = word_sentiments[word]
        print(f"{word}: {count} occurrence/s, Sentiment: {sentiment}")







