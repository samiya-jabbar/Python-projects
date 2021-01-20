import googletrans
import speech_recognition as s_r

#take input from user
r = s_r.Recognizer()
my_mic = s_r.Microphone(device_index=1)

with my_mic as source:
    print("*****SPEAKER*****")
    print("Say Something!!!")
    audio = r.listen(source)

text = r.recognize_google(audio) 
print(text)


#Translation 
from googletrans import Translator
translator = Translator()
result = translator.translate(text, src='en', dest='de')
result.src
print("*****LISTENER*****")
print(result.text)

#output after conversion
import pyttsx3
speaker = pyttsx3.init()
speaker.say(result.text)
speaker.runAndWait()
