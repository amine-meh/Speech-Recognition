import speech_recognition as sr
import webbrowser
import playsound3
import os
import random
from gtts import gTTS 
import time
from time import ctime

r = sr.Recognizer()


def record_audio(ask=False):
  with sr.Microphone() as source:
    if ask:
      assistant_speak(ask)

    audio = r.listen(source)
    voice_data = ''
    try:
      voice_data = r.recognize_google(audio)
    except sr.UnknownValueError:
      assistant_speak('Sorry, I did not get that')
    except sr.RequestError:
      assistant_speak('Sorry, the service is down')
    print(f">> {voice_data.lower()}")
    return voice_data.lower()
  
def assistant_speak(audio_string):
  tts = gTTS(text = audio_string, lang='en')
  r = random.randint(1, 100000000)
  audio_file = 'audio' + str(r) + '.mp3'
  tts.save(audio_file)
  playsound3.playsound(audio_file)
  print(f"Elena: {audio_string}")
  os.remove(audio_file)
  
def respond(user_req):
  if 'What is your name' in user_req:
    assistant_speak("My name is Elena")

  if 'What time is it' in user_req:
    assistant_speak(ctime())

  if 'google' in user_req:
    search = record_audio('What do you want to search for?')
    url = 'https://google.com/search?q=' + search
    webbrowser.get().open(url)
    assistant_speak('Here is what I found for '+ search + ':')

  if 'youtube' in user_req:
    yt_search = record_audio('What do you want to search for on youtube?')
    url = 'https://www.youtube.com/results?search_query=' + yt_search
    webbrowser.get().open(url)
    assistant_speak('Here is what I found for '+ yt_search + ':')

  if 'location' in user_req:
    location = record_audio('What is the location?')
    url = 'https://google.nl/maps/place/' + location + '/&amp;'
    webbrowser.get().open(url)
    assistant_speak('Here is the location of '+ location + ':')

  if 'exit' in user_req:
    assistant_speak('Goodbye')
    exit()



time.sleep(1)
assistant_speak('How can I help you?')
while 1:
  voice_data = record_audio()
  respond(voice_data)

    

