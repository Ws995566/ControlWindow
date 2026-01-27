import speech_recognition as sr

recognizer = sr.Recognizer()
mic = sr.Microphone()

def listen_command():
    with mic as source:
        audio = recognizer.listen(source)

    try:
        return recognizer.recognize_google(audio).lower()
    except:
        return ""
