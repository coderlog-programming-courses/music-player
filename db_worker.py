import sqlite3


def create_datebase():
    connection = sqlite3.connect('db.bin')
    cursor = connection.cursor()

    cursor.execute('CREATE TABLE playlists(id INTEGER PRIMARY KEY NOT NULL, playlist TEXT NOT NULL)')
    cursor.execute('CREATE TABLE connect(id_playlist INTEGER NOT NULL, id_music INTEGER NOT NULL)')
    cursor.execute('CREATE TABLE musics(id INTEGER PRIMARY KEY, music TEXT NOT NULL)')
    connection.commit()

    connection.close()

def add_music(path_to_music):
    
    connection = sqlite3.connect('db.bin')
    cursor = connection.cursor()    
    cursor.execute('INSERT INTO musics (music) VALUES ("{}")'.format(path_to_music))
    cursor.close()
    connection.commit()

    connection.close()

def delete_music(id):

    connection = sqlite3.connect('db.bin')
    cursor = connection.cursor()    
    cursor.execute('DELETE FROM musics WHERE id = "{}"'.format(id))
    cursor.execute('')
    cursor.close()
    connection.commit()
    
    connection.close()