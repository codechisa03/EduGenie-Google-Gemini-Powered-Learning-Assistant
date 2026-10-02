import os
import google.generativeai as genai  # type: ignore
from dotenv import load_dotenv

load_dotenv(override=True)
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

if GEMINI_API_KEY:
    genai.configure(api_key=GEMINI_API_KEY)

# Using standard gemini-1.5-pro instead of the deprecated -latest
MODEL_NAME = "gemini-3.8-flash"

def ask_question(question: str) -> str:
    if not GEMINI_API_KEY or GEMINI_API_KEY == "your_gemini_api_key_here":
        return "Error: Google Gemini API Key is missing or invalid. Please check your .env file."
    
    try:
        model = genai.GenerativeModel(MODEL_NAME)
        prompt = f"Provide a smart and concise answer to the following question:\n\nQuestion: {question}"
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"Error occurred while fetching response: {str(e)}"
