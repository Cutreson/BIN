import pyttsx3
import speech_recognition
def change_voice(engine, language, gender='VoiceGenderFemale'):
    for voice in engine.getProperty('voices'):
        if language in voice.languages and gender == voice.gender:
            engine.setProperty('voice', voice.id)
            return True

    raise RuntimeError("Language '{}' for gender '{}' not found".format(language, gender))
while(True):
    engine = pyttsx3.init()
    change_voice(engine, "vi", "VoiceGenderFemale")
    engine.say("Hello")
    engine.runAndWait()