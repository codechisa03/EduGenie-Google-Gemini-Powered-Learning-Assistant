import os
import google.generativeai as genai  # type: ignore
from dotenv import load_dotenv

load_dotenv(override=True)
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

if GEMINI_API_KEY:
    genai.configure(api_key=GEMINI_API_KEY)

MODEL_NAME = "gemini-flash-latest"

def summarize_text(text: str) -> str:
    if not GEMINI_API_KEY or GEMINI_API_KEY == "your_gemini_api_key_here":
        return "Error: Google Gemini API Key is missing or invalid. Please check your .env file."
    
    try:
        model = genai.GenerativeModel(MODEL_NAME)
        prompt = f"Summarize the following educational passage into a concise and easy-to-understand version, retaining the core information:\n\n{text}"
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"Error occurred while summarizing text: {str(e)}"
