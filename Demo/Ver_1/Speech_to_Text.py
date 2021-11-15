import speech_recognition as sr
from gtts import gTTS
import os
import time
import playsound
from NhanDien import nhanDien

r = sr.Recognizer()

while(True):
    with sr.Microphone() as source:
        print("Recognizing...")
        audio_data = r.record(source,duration=3)
    try:
        text = r.recognize_google(audio_data,language="vi")
    except:
        text = ""
    print(text)
    if (text==""):
        playsound.playsound("F:/QT/BIN/Speech/Basic/02_Speech_to_Text/voice_1.mp3")
    elif "nhận diện khuôn mặt" in text:
        if(nhanDien() == True):
            playsound.playsound("F:/QT/BIN/Speech/Basic/02_Speech_to_Text/voice_2.mp3")
            print("Nhan dien thanh cong")
        else:
            print("Khong thanh cong")
    else:
        playsound.playsound("F:/QT/BIN/Speech/Basic/02_Speech_to_Text/voice_3.mp3")