import sqlite3
import os.path
from playsound import playsound

def play_music():
    id = input()
    connection = sqlite3 .connect('db.bin')
    cursor = connection.cursor()
    id_music = cursor.execute('SELECT music FROM musics WHERE id = {}'.format(id))
    path_music = id_music.fetchone()
    
    playsound("{}".format(path_music[0]))


play_music()
