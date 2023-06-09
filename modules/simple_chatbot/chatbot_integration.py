import requests

# As a temporary solution, create a new file called secret.py in the same directory as this file.
# then add the headers variable containing the header and import it here.
from modules.simple_chatbot.secret import headers


API_URL = "https://api-inference.huggingface.co/models/microsoft/DialoGPT-large"

# Change the header to your own personal headers file here!
# To get your headers file, refer to:
# https://huggingface.co/microsoft/DialoGPT-large

headers = headers
class ChatbotIntegration:
    __generated_responses = []
    __past_user_inputs = []

    def __init__(self) -> None:
        pass

    def query(self, payload):
        response = requests.post(API_URL, headers=headers, json=payload)
        return response.json()
    
    def update_history(self, user_input, generated_response):
        self.__past_user_inputs.append(user_input)
        self.__generated_responses.append(generated_response)

    def retrieve_inputs(self, text):
        inputs = {'text': text}
        if self.__past_user_inputs:
            inputs.update({
                "past_user_inputs": self.__past_user_inputs,
                "generated_responses": self.__generated_responses,
            })
        return inputs

    def get_response(self, text):
        output = self.query({
            "inputs": self.retrieve_inputs(text),
            "parameters": {
                "max_new_tokens": 100
            },
            "options": {
                "wait_for_model": True
            }
        })
        generated_text = output.get("generated_text")
        self.update_history(text, generated_text)
        return generated_text