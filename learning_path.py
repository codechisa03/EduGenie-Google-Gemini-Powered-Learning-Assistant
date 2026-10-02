import os
from google import genai
from dotenv import load_dotenv

load_dotenv(override=True)
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=GEMINI_API_KEY) if GEMINI_API_KEY else None

MODEL_NAME = "gemini-2.5-flash"

def get_learning_recommendations(topic: str) -> str:
    if not GEMINI_API_KEY or GEMINI_API_KEY == "your_gemini_api_key_here":
        return "Error: Google Gemini API Key is missing or invalid. Please check your .env file."
    
    try:
        prompt = f"""
Create a personalized, structured learning path for the following topic: {topic}.
Organize the concepts logically from beginner to advanced levels.
Include suggested learning resources such as videos, articles, or books for each level.
Use markdown to style the learning path effectively for readability.
"""
        response = client.models.generate_content(model=MODEL_NAME, contents=prompt)
        return response.text
    except Exception as e:
        return f"Error occurred while generating learning recommendations: {str(e)}"
