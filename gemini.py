import google.generativeai as genai

# Configure your API key here
genai.configure(api_key="AIzaSyC0_qSA3FM2g6UdZI5IQETfwjJKT_OfkLI")

# Use the full model name from the list
model = genai.GenerativeModel("models/gemini-2.5-pro")

def chat_with_gemini(prompt: str) -> str:
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"Error: {e}"

# Example usage
print(chat_with_gemini("Hello Gemini! What can you do?"))
