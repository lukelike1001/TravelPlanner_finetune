import os
import requests

# Load the API key from environment variables
HUGGINGFACE_API_KEY = os.getenv("HUGGINGFACE_API_KEY")
MODEL_ID = "xingyaoww/CodeActAgent-Mistral-7b-v0.1"

# Ensure the API key is set
if HUGGINGFACE_API_KEY is None:
    raise ValueError("HUGGINGFACE_API_KEY environment variable is not set")

# Define the HuggingFace API endpoint
API_URL = f"https://api-inference.huggingface.co/models/{MODEL_ID}"

headers = {
    "Authorization": f"Bearer {HUGGINGFACE_API_KEY}",
    "Content-Type": "application/json"
}

def query(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()

# Example payload
payload = {
    "inputs": "Translate the following English text to French: 'Hello, how are you?'"
}

# Call the API
result = query(payload)
print(f"Result: {result}")