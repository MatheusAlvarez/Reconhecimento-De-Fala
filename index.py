# |===============================|
# |     RECONHECIMENTO DE VOZ     |
# |===============================|
# | CRIADOR: Matheus Maia Alvarez |
# | GITHUB: MatheusAlvarez        |
# | CONTATO: (11)99423-7418       |
# |===============================|

# Biblioteca speech-recognition (instalar no terminal "pip install SpeechRecognition" e o pyaudio)
import speech_recognition as sr

# Biblioteca time (utilizada para dar animação de tempo)
from time import sleep

rec = sr.Recognizer()

with sr.Microphone() as mic:
    rec.adjust_for_ambient_noise(mic)
    print('Pode falar! Estou gravando...')
    audio = rec.listen(mic)
    texto = rec.recognize_google(audio, language="pt-BR")
    print('Escrevendo texto...')
    sleep(1)
    print(texto)
