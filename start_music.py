import wave
from pygame import mixer
import sqlite3
import os.path
from db_worker import wave_music

def pause():
                mixer.music.pause()

def play(id):
        
        mixer.init()
        mixer.music.load("{}".format(id))
        mixer.music.play()
        while True:
                pass




