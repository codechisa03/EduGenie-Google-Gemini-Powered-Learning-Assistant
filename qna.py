import os
from google import genai
from dotenv import load_dotenv

load_dotenv(override=True)
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=GEMINI_API_KEY) if GEMINI_API_KEY else None

MODEL_NAME = "gemini-2.5-flash"

def ask_question(question: str) -> str:
    if not GEMINI_API_KEY or GEMINI_API_KEY == "your_gemini_api_key_here":
        return "Error: Google Gemini API Key is missing or invalid. Please check your .env file."
    
    try:
        prompt = f"Provide a smart and concise answer to the following question:\n\nQuestion: {question}"
        response = client.models.generate_content(model=MODEL_NAME, contents=prompt)
        return response.text
    except Exception as e:
        return f"Error occurred while fetching response: {str(e)}"
