import os
import requests
from dotenv import load_dotenv

load_dotenv(dotenv_path="")

API_URL = "https://api-inference.huggingface.co/models/Helsinki-NLP/opus-mt-en-vi"
HF_TOKEN = os.getenv("HF_TOKEN")

headers = {"Authorization": f"Bearer {HF_TOKEN}"}

def translate_text(input_data):
    text = input_data.get("text")
    dest_language = input_data.get("dest_language", "vi")
    
    def call_api(single_text):
        payload = {"inputs": single_text}
        response = requests.post(API_URL, headers=headers, json=payload)
        
        if response.status_code == 200:
            result = response.json()
            try:
                if isinstance(result, list) and len(result) > 0 and "translation_text" in result[0]:
                    translated_text = result[0]["translation_text"].strip()
                    return translated_text
                else:
                    raise ValueError(f"Unexpected response format: {result}")
            except (KeyError, IndexError) as e:
                raise ValueError(f"Error parsing API response: {e}, Response: {result}")
        else:
            raise Exception(f"API request failed with status {response.status_code}: {response.text}")
    
    if isinstance(text, str):
        return call_api(text)
    elif isinstance(text, list):
        return [call_api(single_text) for single_text in text]
    else:
        raise ValueError("Input 'text' must be a string or a list of strings")

if __name__ == "__main__":
    # Test case 3.1: Dịch một văn bản
    input_single = {
        "text": "Hello",
        "dest_language": "vi"
    }
    print("Translated single text:", translate_text(input_single))  
        
    # Test case 3.2: Dịch danh sách văn bản
    input_list = {
        "text": ["Hello", "I am Peter"],
        "dest_language": "vi"
    }
    print("Translated list of texts:", translate_text(input_list))