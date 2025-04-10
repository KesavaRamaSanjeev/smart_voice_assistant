# gemini_ai.py
import google.generativeai as genai

genai.configure(api_key="AIzaSyAHWWbsXYCO6N11bBf_rkQiTuZaQ9zsY4A")  # Replace if needed

model = genai.GenerativeModel('gemini-1.5-flash')

def ask_gemini(prompt):
    try:
        # Ask Gemini to keep answers short
        final_prompt = f"{prompt}\n\nPlease respond briefly in just 1 or 2 lines."
        response = model.generate_content(final_prompt)
        return response.text.strip()
    except Exception as e:
        return "Sorry, Gemini could not respond right now."
