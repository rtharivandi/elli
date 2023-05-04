# Import module for chatbot
from modules.simple_chatbot.chatbot_integration import get_response
from modules.voice_generation.voice_generation import init_engine,generate_voice

def chat():
    print("******")
    tts_engine = init_engine()
    while True:
        text = input()
        print(f"You:{text}")
        response = get_response(text)
        print(f"Bot:{response}")
        generate_voice(tts_engine, response)

chat()