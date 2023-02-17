# -*- coding: utf-8 -*-
"""
Created on Thu Feb 16 21:39:49 2023

@author: rocha
"""
import speech_recognition as sr
from speech_recognition import Microphone, Recognizer
from gtts import gTTS as TTS
from io import BytesIO
import pyglet
from time import sleep

lang = 'pt-BR'
rec = Recognizer()

def text_to_speech(text):
    with BytesIO() as mp3_fp:
        TTS(text, lang=lang).write_to_fp(mp3_fp)
        mp3_fp.seek(0)
        pyglet.media.load('_.mp3', file=mp3_fp).play()
    sleep(1)

def speech_to_text(audio):
    # using google speech recognition
    text = rec.recognize_google(audio_text, language=lang)
    sleep(1)
    return text

with Microphone() as source:
    text_to_speech("Fale")
    audio_text = rec.listen(source)
    text_to_speech("Tempo acabou, obrigado")
    
    try:
        text = speech_to_text(audio_text)
        text_to_speech("Você disse: "+text)
    except:
         text_to_speech("Desculpe, eu não consigo te ouvir")


