import speech_recognition as sr 
from selenium import webdriver
import time
from speech_recognition import Microphone, Recognizer, AudioFile, UnknownValueError, RequestError
from gtts import gTTS
from playsound import playsound
import pyttsx3
import urllib.request
import urllib.request as ur
import urllib.parse as par
import json 
import  unidecode

key='AIzaSyDan48Fnx6Evpv5HY9RPOJCfGX9HGFZ8mA'
#nombre= 'elo'
r = sr.Recognizer()
engine = pyttsx3.init()
import requests
        # Creamos la petición HTTP con GET:

        # Imprimimos el resultado si el código de estado HTTP es 200 (OK):


def habla(text):
    
    engine.setProperty('voice','spanish' )
    engine.say(text)
    engine.runAndWait()


def escucha():
    try:
        dato=""
        print("Escuchando...")
        with sr.Microphone() as source:             
            r.adjust_for_ambient_noise(source)  
            print ("say something3")
            audio = r.listen(source,timeout=5)
            dato = r.recognize_google(audio, language='es-ES') 
            #dato = dato.lower()
            #if nombre in dato:
            #    dato = dato.replace(nombre,'')
            #    habla(dato)
            #print(dato)
    except: 
        pass
    return dato

def run():
    dato = escucha()
    dato = dato.lower()
    
    #if 'alex' in dato:
        #quita = dato.replace('alex','')
    buscar = unidecode.unidecode(dato) 
    
    print(buscar)
    data = requests.get(f"http://localhost:4000/api/pregunta/{buscar}")
    str_data = data.text
    obje = json.dumps(str_data)
    
    respuesta = obje.replace('respuesta','') 

    habla('Respondiendo' + respuesta) 



run()
