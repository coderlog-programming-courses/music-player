import sqlite3
import os.path

def datebase():
    connection = sqlite3.connect('db.bin')
    cursor = connection.cursor()

    cursor.execute('CREATE TABLE playlists(id int PRIMARE KEY, playlist text NOT NULL)')
    connection.commit()
    cursor.execute('CREATE TABLE connect(id_playlist int NOT NULL, id_music int NOT NULL)')
    connection.commit()
    cursor.execute('CREATE TABLE musics(id int PRIMARE KEY, music text NOT NULL)')
    connection.commit()

    connection.close()

if os.path.exists('db.bin') != True:
    datebase()