# blog_generator.py
import os
import time
from openai import OpenAI
from dotenv import load_dotenv

# Load API key
load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_blog(topic):
    prompt = (
        f"Write a high-quality blog post on the topic: '{topic}'.\n\n"
        "The blog should:\n"
        "- Start with a hook.\n"
        "- Be engaging and informative.\n"
        "- Contain a clear structure with headings of what is discussed in it.\n"
        "- Be 50–60 words long.\n"
        "- Use simple but professional language.\n"
        "- End with a conclusion or call to action."
    )
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.7
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"Error: {e}"

def save_blog_to_file(topic, blog):
    timestamp = time.strftime("%Y-%m-%d_%H-%M-%S")
    filename = f"AI_blog_{topic}_{timestamp}.txt"
    with open(filename, "w", encoding="utf-8") as f:
        f.write(f"Topic: {topic}\n\n{blog}")
    return filename