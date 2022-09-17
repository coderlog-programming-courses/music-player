import sqlite3
import os.path

def wave_music(id):

        connection = sqlite3 .connect('db.bin')
        cursor = connection.cursor()
        id_music = cursor.execute('SELECT music FROM musics WHERE id = {}'.format(id))
        path_music = id_music.fetchone()
        return (path_music[0])