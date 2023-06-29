import os
from pygame import mixer
from gtts import gTTS

my_file = open('C:/Users/User/Desktop/Python/103text.txt', 'r')

my_string = my_file.read()


my_file.close()


mixer.init()

tts = gTTS(text = my_string, lang='en')
tts.save('C:/Users/User/Desktop/Python/Helper/mp3_name.mp3')
mixer.music.load('mp3_name.mp3')
mixer.music.play()
