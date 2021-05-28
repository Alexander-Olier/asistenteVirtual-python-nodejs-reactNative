import speech_recognition as sr 
from speech_recognition import Microphone, Recognizer, AudioFile, UnknownValueError, RequestError
from playsound import playsound
import pyttsx3
import urllib.request
import json 
import  unidecode
import requests
#nombre= 'elo'
r = sr.Recognizer()
engine = pyttsx3.init()


def habla(text):
    
    engine.setProperty('voice','spanish' )
    engine.say(text)
    engine.runAndWait()

def escucha():
    try:
        dato=""
        habla('Hola, soy tu asistente')
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
    
    buscar = unidecode.unidecode(dato) 
    print(dato)
    if dato:
        data = requests.get(f"http://localhost:4000/api/pregunta/prg/{buscar}")
        print(data)
        str_data = data.text
        print(str_data)

        if str_data == '':
           habla('lo siento, no tengo una respuesta para tu pregunta')
       
        else:#acomodar a que cuando sea 404 entre aqui
            str_data = data.text
            obje = json.dumps(str_data)
            respuesta = obje.replace('respuesta','') 
            habla('Respondiendo' + respuesta) 
    else:
        run() 
    
    

run()
