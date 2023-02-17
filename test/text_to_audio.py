# -*- coding: utf-8 -*-
import gtts
from io import BytesIO
import pyglet

mp3_fp = BytesIO()
tts = gtts.gTTS("Olá mundo", lang='ja')
tts.write_to_fp(mp3_fp)
mp3_fp.seek(0)
pyglet.media.load('_.mp3', file=mp3_fp).play()
