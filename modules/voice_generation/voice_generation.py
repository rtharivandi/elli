import pyttsx3

def init_engine():
    engine = pyttsx3.init()
    return engine

def generate_voice(engine, text):
    engine.say(text)
    engine.runAndWait()
