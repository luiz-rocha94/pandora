# -*- coding: utf-8 -*-
"""
Created on Fri Feb 17 08:24:39 2023

@author: rocha
"""

from speech_recognition import Microphone, Recognizer
from gtts import gTTS
from io import BytesIO
from pyglet.media import load
from time import sleep
from revChatGPT.V1 import Chatbot
import json


class VoiceBot():
    def __init__(self, chat_config, input_lang='pt-BR', output_lang='ja'):
        self.input_lang, self.output_lang = input_lang, output_lang
        self.STT = Recognizer()
        self.TTS = gTTS
        self.chatbot = Chatbot(config=chat_config)

    def text_to_speech(self, text):
        with BytesIO() as mp3_fp:
            self.TTS(text, lang=self.output_lang, slow=True).write_to_fp(mp3_fp)
            mp3_fp.seek(0)
            source = load('_.mp3', file=mp3_fp)
        source.play()
        sleep(source.duration)
        
    def text_generator(self, input_text):
        print('Escute')
        for data in self.chatbot.ask(input_text):
            output_text = data["message"]
        return output_text

    def speech_to_text(self):
        print('Fale')
        with Microphone() as source:         
            input_audio = self.STT.listen(source)
        try:
            text = self.STT.recognize_google(input_audio, language=self.input_lang)
        except:
            text = None
        return text
    
    def talk(self):
        input_text = self.speech_to_text()
        if input_text is not None:
            output_text = self.text_generator(input_text)
            self.text_to_speech(output_text)
    
    def multi_talk(self, runs=5):
        for i in range(runs):
            self.talk()

config = json.load(open('config.json'))
bot = VoiceBot(config)
bot.multi_talk()
