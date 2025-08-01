# sentiment_analyzer.py
import os
from dotenv import load_dotenv
from openai import OpenAI
import datetime

# Load API key
load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def analyze_sentiment(text):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": f"What is the sentiment of this sentence? Just reply with Positive, Negative, or Neutral.\n\nSentence: \"{text}\""}
        ],
        temperature=0
    )
    return response.choices[0].message.content.strip()

def save_result(text, sentiment):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = f"sentiment_{timestamp}.txt"
    with open(filename, "w", encoding="utf-8") as f:
        f.write(f"Input Sentence: {text}\n")
        f.write(f"Sentiment: {sentiment}\n")
    return filename