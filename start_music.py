import wave
from pygame import mixer
import sqlite3
import os.path
from db_worker import wave_music

id = input()

def pause():
        v = input()
        if v == "q":
                mixer.music.pause()

def play(id):
        
        mixer.init()
        mixer.music.load("{}".format(wave_music(id)))
        mixer.music.play()
        while True:
                pause()



play(id)
