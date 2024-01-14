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


def generate_wordcloud(word_counts):
    wordcloud = WordCloud(width=800, height=400, random_state=42, background_color='white').generate_from_frequencies(
        word_counts)
    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    plt.show()


def preprocess_text(summary):
    stop_words = set(stopwords.words('english'))
    word_tokens = word_tokenize(summary)
    punctuation = set(string.punctuation)
    filtered_text = [word for word in word_tokens if word.lower() not in stop_words and word.lower() not in punctuation]
    preprocess_text = ' '.join(filtered_text)
    return preprocess_text


def analyze_sentiment(summary):
    sia = SentimentIntensityAnalyzer()
    sentiment_score = sia.polarity_scores(preprocess_text(summary))
    if sentiment_score['compound'] >= 0.05:
        sentiment = 'Positive'
    elif sentiment_score['compound'] <= -0.05:
        sentiment = 'Negative'
    else:
        sentiment = 'Neutral'
    return sentiment


def tokenisation_sentiment_analysis_wordwise(summary):
    preprocessed_text = preprocess_text(summary)
    word_tokens = word_tokenize(preprocessed_text)
    word_sentiments = {word: analyze_sentiment(word) for word in word_tokens}
    word_counts = {word: word_tokens.count(word) for word in set(word_tokens)}
    generate_wordcloud(word_counts)
    return word_tokens, word_sentiments


def display_word_sentiment(summary):
    word_tokens, word_sentiments = tokenisation_sentiment_analysis_wordwise(summary)
    word_counts = {word: word_tokens.count(word) for word in set(word_tokens)}
    top_words = sorted(word_counts.items(), key=lambda x: x[1], reverse=True)[:5]
    print("\nTop words along with Sentiment:")
    for word, count in top_words:
        sentiment_for_word = word_sentiments.get(word, 'Unknown')
        print(f"{word}: {count} occurrence/s, Sentiment: {sentiment_for_word}")
