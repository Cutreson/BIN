import speech_recognition as sr
from gtts import gTTS
import os
import time
import playsound

def speak(text):
    tts = gTTS(text=text,lang="vi")
    filename = "F:/QT/BIN/Speech/Basic/01_Text_to_Speech/voice.mp3"
    tts.save(filename)
    playsound.playsound(filename)
    ##############################
    tts = gTTS("Nói đi",lang="vi")
    tts.save("F:/QT/BIN/Speech/Basic/01_Text_to_Speech/voice_1.mp3")
    tts = gTTS("Nhận diện thành công",lang="vi")
    tts.save("F:/QT/BIN/Speech/Basic/01_Text_to_Speech/voice_2.mp3")
    tts = gTTS("Không hiểu",lang="vi")
    tts.save("F:/QT/BIN/Speech/Basic/01_Text_to_Speech/voice_3.mp3")
speak("Ngoao ngoao ơi")
