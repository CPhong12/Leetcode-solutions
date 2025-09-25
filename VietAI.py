import requests

API_URL = "https://api-inference.huggingface.co/models/VietAI/envit5-translation"
headers = {"Authorization": "Bearer hf_your_token_here"}

def query(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()

output = query({
    "inputs": "Translate English to Vietnamese: I love studying artificial intelligence.",
})
print(output)
