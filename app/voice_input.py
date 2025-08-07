import speech_recognition as sr

def get_voice_input():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("🎤 Speak the incident details...")
        audio = r.listen(source)
    try:
        text = r.recognize_google(audio)
        print("✅ Detected text:", text)
        return text
    except:
        return "❌ Could not understand the audio"
