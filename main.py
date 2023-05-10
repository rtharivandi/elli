from modules.simple_chatbot.chatbot_integration import ChatbotIntegration
from modules.voice_generation.voice_generation import init_engine,generate_voice


def chat():
    print("*** STARTING ***")
    tts_engine = init_engine()
    chatbot = ChatbotIntegration()
    while True:
        text = input(">> You:")
        response = chatbot.get_response(text)
        print(f">>Bot:{response}")
        generate_voice(tts_engine, response)

if __name__ == "__main__":
    chat()