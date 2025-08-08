import speech_recognition as sr
import pyttsx3
from recommend_bns import recommend

recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

print("🎙️ Voice Assistant Ready. Say something...")

while True:
    with sr.Microphone() as source:
        print("🎧 Listening...")
        audio = recognizer.listen(source)

    try:
        query = recognizer.recognize_google(audio).lower()
        print("🗣️ You said:", query)

        if query in ["exit", "stop", "quit"]:
            speak("Okay, exiting now.")
            break

        results = recommend(query, top_n=1)
        if results is None:
            response = "Sorry, I couldn't find any matching law section."
        else:
            response = results.iloc[0]['content']

        print("📖", response)
        speak(response)

    except Exception as e:
        print("❌ Error:", e)
        speak("Sorry, I couldn't understand.")
