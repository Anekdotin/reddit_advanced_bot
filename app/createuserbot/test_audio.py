import speech_recognition as sr
import os
from app.createuserbot.query_api import bing, google, ibm
import subprocess

download_location = "/home/bot/Downloads/"

r = sr.Recognizer()
def convertfile():
    print("Converting Captcha...")

    # after it downloads to folder..convert it for google
    os.system("echo 'y' | ffmpeg -i " + download_location + "audio.mp3 " + download_location + "audio.wav 2>/dev/null")
    arch = subprocess.check_output("echo 'y' | ffmpeg -i " + download_location + "audio.mp3 ./audio.wav 2>/dev/null", shell=True);
    print(arch)
    print("converterd?")
    with sr.AudioFile(download_location + 'audio.wav') as source:
        audio = r.record(source)

    print("Submitting To Speech to Text:")
    determined = google(audio)
    # Instead of google, you can use ibm or bing here
    print("Text from google says ..:", determined)


