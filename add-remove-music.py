import sqlite3

def add_music():

    path_to_music = input()
    connection = sqlite3.connect('db.bin')
    cursor = connection.cursor()    
    cursor.execute('INSERT INTO musics (music) VALUES ("{}")'.format(path_to_music))
    cursor.close()
    connection.commit()
    connection.close()

add_music()