# -*- coding: utf-8 -*-
from revChatGPT.V1 import Chatbot
import json


config = json.load(open('config.json'))
chatbot = Chatbot(config=config)

print("Chatbot: ")
for data in chatbot.ask("Bom dia"):
    message = data["message"]
print(message)
