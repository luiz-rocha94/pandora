# -*- coding: utf-8 -*-
"""
Created on Thu Feb 16 21:39:49 2023

@author: rocha
"""
import speech_recognition as sr
from speech_recognition import Microphone, Recognizer
from gtts import gTTS
from io import BytesIO
import pyglet
from time import sleep


class VoiceBot():
    def __init__(self, input_lang='pt-BR', output_lang='ja'):
        self.input_lang, self.output_lang = input_lang, output_lang
        self.STT = Recognizer()
        self.TTS = gTTS

    def text_to_speech(self, text):
        with BytesIO() as mp3_fp:
            self.TTS(text, lang=self.output_lang).write_to_fp(mp3_fp)
            mp3_fp.seek(0)
            pyglet.media.load('_.mp3', file=mp3_fp).play()
        sleep(1)

    def speech_to_text(self, audio):
        text = self.STT.recognize_google(audio, language=self.input_lang)
        sleep(1)
        return text
    
    def talk(self):
        with Microphone() as source:
            self.text_to_speech("Bom dia, qual o seu pedido?")
            audio = self.STT.listen(source)
            
            try:
                text = self.speech_to_text(audio)
                self.text_to_speech("Você disse: "+text)
            except:
                self.text_to_speech("Desculpe, eu não consigo te ouvir")

bot = VoiceBot()
bot.talk()


