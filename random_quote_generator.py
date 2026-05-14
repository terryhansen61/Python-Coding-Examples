import tkinter as tk
import requests
import time
from textblob import TextBlob

# -----------------------------
# 1. YOUR SENTIMENT ANALYZER
# Replace this with your real model
# -----------------------------
def analyze_sentiment(text):
    blob = TextBlob(text)
    sentiment_score = blob.sentiment.polarity
    if sentiment_score > 0:
        return 'positive'
    elif sentiment_score < 0:
        return 'negative'
    else:
        return 'neutral'

# -----------------------------
# 2. FETCH QUOTE FROM ZENQUOTES
# -----------------------------
def fetch_quote():
    try:
        response = requests.get("https://zenquotes.io/api/random", timeout=5)
        data = response.json()[0]
        return f"{data['q']} — {data['a']}"
    except:
        return None

# -----------------------------
# 3. MATCH QUOTE TO SENTIMENT
# -----------------------------
def get_matching_quote(target_sentiment, max_attempts=10):
    for _ in range(max_attempts):
        quote = fetch_quote()
        if not quote:
            continue

        quote_text = quote.split("—")[0].strip()
        quote_sentiment = analyze_sentiment(quote_text)

        if quote_sentiment == target_sentiment:
            return quote

        time.sleep(0.2)  # avoid hammering the API

    return "Couldn't find a matching quote. Try again."

# -----------------------------
# 4. UI CALLBACK
# -----------------------------
def process_input():
    selected = sentiment_var.get()

    if selected == "happy":
        user_sentiment = "positive"
    elif selected == "neutral":
        user_sentiment = "neutral"
    else:
        user_sentiment = "negative"

    quote = get_matching_quote(user_sentiment)

    result_label.config(
        text=f"Selected mood: {selected}\n\n{quote}"
    )

# -----------------------------
# 5. TKINTER UI
# -----------------------------
root = tk.Tk()
root.title("Sentiment-Based Quote Generator (Radio Buttons)")
root.geometry("650x350")

tk.Label(root, text="How are you feeling today?", font=("Arial", 14)).pack(pady=10)

# Radio button variable
sentiment_var = tk.StringVar(value="neutral")

# Radio buttons
tk.Radiobutton(root, text="Happy", variable=sentiment_var, value="happy", font=("Arial", 12)).pack()
tk.Radiobutton(root, text="Neutral", variable=sentiment_var, value="neutral", font=("Arial", 12)).pack()
tk.Radiobutton(root, text="Sad", variable=sentiment_var, value="sad", font=("Arial", 12)).pack()

tk.Button(root, text="Get Matching Quote", command=process_input, font=("Arial", 12)).pack(pady=15)

result_label = tk.Label(root, text="", wraplength=600, justify="center", font=("Arial", 14))
result_label.pack(pady=20)

root.mainloop()
