import os
import json
from google import genai
from dotenv import load_dotenv

load_dotenv(override=True)
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=GEMINI_API_KEY) if GEMINI_API_KEY else None

MODEL_NAME = "gemini-2.5-flash"

def clean_json_block(text: str) -> str:
    """Removes markdown code blocks to cleanly parse JSON."""
    text = text.strip()
    if text.startswith("```json"):
        text = text[7:]
    elif text.startswith("```"):
        text = text[3:]
    
    if text.endswith("```"):
        text = text[:-3]
    return text.strip()

def generate_quiz(passage: str):
    if not GEMINI_API_KEY or GEMINI_API_KEY == "your_gemini_api_key_here":
        return {"error": "Google Gemini API Key is missing or invalid. Please check your .env file."}
    
    try:
        prompt = f"""
Given the following passage, generate a quiz with exactly 3 multiple-choice questions (MCQs).
Each question must have exactly 4 options.
Return the output STRICTLY in the following JSON format as a list of dictionaries, without any extra text or conversational filler:
[
  {{
    "question": "The question text here",
    "options": ["Option A", "Option B", "Option C", "Option D"],
    "answer": "Option A"
  }},
  ...
]

Passage:
{passage}
"""
        response = client.models.generate_content(model=MODEL_NAME, contents=prompt)
        cleaned_json = clean_json_block(response.text)
        quiz_data = json.loads(cleaned_json)
        return {"quiz": quiz_data}
    except json.JSONDecodeError:
        return {"error": "Failed to parse the generated quiz. The model did not return a valid JSON format.", "raw": response.text}
    except Exception as e:
        return {"error": f"Error occurred while generating quiz: {str(e)}"}
