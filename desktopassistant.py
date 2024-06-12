#print what i said
import speech_recognition as sr
import os
from elasticsearch import Elasticsearch
from elasticsearch.helpers import bulk
r = sr.Recognizer()
mic = sr.Microphone()
with mic as source:
    r.adjust_for_ambient_noise(source)
    audio = r.listen(source)
    transcript = r.recognize_google(audio)
    print(transcript)
#reply to me 
import subprocess
def say(text):
    subprocess.call(['say', text])
say("hi whatsup?")
