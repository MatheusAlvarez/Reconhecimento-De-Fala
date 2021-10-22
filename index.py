# |=============================================|
# |               CÓDIGO SIMPLES                | 
# |=============================================|
# | PROPOSTA : RECONHECIMENTO DE FALA           |
# | FEITO POR: MATHEUS MAIA ALVAREZ             |
# | GITHUB: https://github.com/MatheusAlvarez   |
# | CONTATO: (11)99423-7418                     |
# |=============================================|


# Biblioteca speech-recognition (instalar no terminal "pip install SpeechRecognition" e o pyaudio)
import speech_recognition as sr

# Biblioteca time (utilizada para dar animação de tempo)
from time import sleep

rec = sr.Recognizer()

with sr.Microphone() as mic:
    rec.adjust_for_ambient_noise(mic)
    
    # O programa vai imprimir na tela que está gravando
    print('Pode falar! Estou gravando...')
    
    audio = rec.listen(mic)
    texto = rec.recognize_google(audio, language="pt-BR")
    
    # O programa vai imprimir na tela que está digitando a sua fala
    print('Escrevendo texto...')
    
    # Sleep vai dar animação para não escrever a sua fala direto
    sleep(1)
    
    print(texto)
