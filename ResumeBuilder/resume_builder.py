import os
import json
from openai import OpenAI
from dotenv import load_dotenv

# Load the API key
load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_resume(name: str, about: str) -> dict:
    prompt = (
    "You are a professional resume writer. Generate a polished resume in valid JSON format. "
    "Enhance the summary section using the information provided, and infer skills, education, and experience from the input. "
    "Only include fields that the user clearly mentioned.\n\n"
    "Input:\n"
    f"Name: {name}\n"
    f"User Description: {about}\n\n"
    "Return JSON with keys: name, summary, skills, experience, education, certifications (if available). "
    "Strictly return only the JSON — no explanation or markdown formatting."
)
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.3
    )
    content = response.choices[0].message.content.strip()
    return json.loads(content)
