import speech_recognition as sr
engine = sr.Recognizer()

with sr.Microphone() as mic:
    print("Say something...")
    engine.adjust_for_ambient_noise(mic)
    audio = engine.listen(mic)
    recog = engine.recognize_google(audio)
    print(f"You said {recog}")

