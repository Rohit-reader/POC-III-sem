from app.voice_input import get_voice_input
from scripts.predict import predict_laws

incident_text = get_voice_input()
if incident_text:
    print("📄 Incident:", incident_text)
    print("⚖️ Recommended IPC Sections:", predict_laws(incident_text))
