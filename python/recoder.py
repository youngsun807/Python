# -*- coding: utf-8 -*-
import speech_recognition as sr

# Convert `data` to 32 bit integers:

r = sr.Recognizer()
audio = ("test.wav")

with sr.AudioFile(audio) as source:
    print('Say something!')
    audio = r.record(source)
    print('Done!')

try:
    language_code = 'ko-KR'  # 한국어로 변경
    text = r.recognize_google(audio)
    print(text.encode('utf-8'))

except Exception as e:
    print(e)