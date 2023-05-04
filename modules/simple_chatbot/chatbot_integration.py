import requests

API_URL = "https://api-inference.huggingface.co/models/microsoft/DialoGPT-large"
headers = {"Authorization": "Bearer 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"}


def query(payload):
	response = requests.post(API_URL, headers=headers, json=payload)
	return response.json()

def get_response(text):
    output = query({
        "inputs": {
            "text": text
        },
        "parameters": {
            "max_new_tokens": 100
        },
        "options": {
            "wait_for_model": True
        }
    })
    return output.get("generated_text")