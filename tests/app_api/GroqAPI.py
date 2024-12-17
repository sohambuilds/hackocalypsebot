import requests



GROQ_API_KEY = "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"
GROQ_API_URL = "https://api.groq.com/openai/v1/chat/completions"

HEADERS = {
    "Authorization": f"Bearer {GROQ_API_KEY}",
    "Content-Type": "application/json"
}

# 4. GroqAPI Class
class GroqAPI:
    @staticmethod
    def generate_response(query, context):
        messages = [{"role": "user", "content": query}]
        for doc in context:
            messages.append({"role": "system", "content": doc})

        try:
            response = requests.post(GROQ_API_URL, json={
                "model": "llama3-8b-8192",  # Example model ID
                "messages": messages
            }, headers=HEADERS)

            response_data = response.json()
            if "choices" not in response_data:
                raise ValueError(f"Unexpected response format: {response_data}")

            return response_data["choices"][0]["message"]["content"]
        except Exception as e:
            return f"Error generating response: {e}"

