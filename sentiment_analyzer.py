# This is a sentiment analyzer.  It takes input text and returns a value from
# -1 to 1.  The textblob has built in functionality to understand certain words
# and returns the sentiment of that text back to you
# I added the function to clear the screen
from textblob import TextBlob
import os

def clear_screen():
    """This clears the output screen"""
    os.system('cls' if os.name == 'nt' else 'clear')

def analyze_sentiment(text):
    blob = TextBlob(text)
    sentiment_score = blob.sentiment.polarity
    if sentiment_score > 0:
        return 'positive'
    elif sentiment_score < 0:
        return 'negative'
    else:
        return 'neutral'

if __name__ == '__main__':
    clear_screen()
    post = input('Enter a sentence to analyze: ')
    print(f'{analyze_sentiment(post) = }')

