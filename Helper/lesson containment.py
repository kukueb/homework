import os
from pygame import mixer
from gtts import gTTS

my_file = open('text.txt', 'r')

my_string = my_file.read()


my_file.close()


mixer.init()

tts = gTTS(text = my_string, lang='ru')
tts.save('mp3_text.mp3')
tts.music.load('mp3_text.mp3')
tts.music.play('mp3_text.mp3')
