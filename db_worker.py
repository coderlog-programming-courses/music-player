import sqlite3
import os.path

def create_datebase():
    connection = sqlite3.connect('db.bin')
    cursor = connection.cursor()

    cursor.execute('CREATE TABLE playlists(id INTEGER PRIMARY KEY NOT NULL, playlist TEXT NOT NULL)')
    cursor.execute('CREATE TABLE connect(id_playlist INTEGER NOT NULL, id_music INTEGER NOT NULL)')
    cursor.execute('CREATE TABLE musics(id INTEGER PRIMARY KEY, music TEXT NOT NULL)')
    connection.commit()

    connection.close()

def wave_music(id):

    connection = sqlite3.connect('db.bin')
    cursor = connection.cursor()
    id_music = cursor.execute('SELECT music FROM musics WHERE id = {}'.format(id))
    path_music = id_music.fetchone()
    return (path_music[0])