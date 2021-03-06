# |=============================================|
# |               CÓDIGO SIMPLES                | 
# |=============================================|
# | PROPOSTA : RECONHECIMENTO DE FALA           |
# | FEITO POR: MATHEUS MAIA ALVAREZ             |
# | GITHUB: https://github.com/MatheusAlvarez   |
# | CONTATO: mthalvarez0000@hotmail.com         |
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
    
    # A variável "audio" vai receber oq você falar no microfone
    audio = rec.listen(mic)
    
    # A variável texto vai receber a sua fala
    texto = rec.recognize_google(audio, language="pt-BR")
    
    # O programa vai imprimir na tela que está digitando a sua fala
    print('Escrevendo texto...')
    
    # Sleep vai dar animação para não escrever a sua fala direto
    sleep(1)
    
    # Vai imprimir na tela a sua fala
    print(texto)
    
#Fim do programa
