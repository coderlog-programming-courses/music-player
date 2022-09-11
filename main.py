import sqlite3
import os.path
from playlist import adding_a_playlist, delete_a_playlist, playlist_output_in_the_form_of_a_letter



def datebase():
    connection = sqlite3.connect('db.bin')
    cursor = connection.cursor()

    cursor.execute('CREATE TABLE playlists(id INTEGER PRIMARY KEY NOT NULL, playlist TEXT NOT NULL)')
    cursor.execute('CREATE TABLE connect(id_playlist INTEGER NOT NULL, id_music INTEGER NOT NULL)')
    cursor.execute('CREATE TABLE musics(id INTEGER PRIMARY KEY, music TEXT NOT NULL)')
    connection.commit()

    connection.close()

if os.path.exists('db.bin') != True:
    datebase()