import sqlite3


def create_datebase():
    connection = sqlite3.connect('db.bin') #Підключення до бази.
    cursor = connection.cursor() #Підключення курсору.

    #Створити таблицю playlistsю
    cursor.execute('CREATE TABLE playlists(id INTEGER PRIMARY KEY NOT NULL, playlist TEXT NOT NULL)')
    #Створити таблицю connect.
    cursor.execute('CREATE TABLE connect(id_playlist INTEGER NOT NULL, id_music INTEGER NOT NULL)')
    #Створити таблицю musics.
    cursor.execute('CREATE TABLE musics(id INTEGER PRIMARY KEY, music TEXT NOT NULL)')
    connection.commit() #Затвердити зміни у бд.

    cursor.close() #Закртити курсос.
    connection.close() #Закрити підключення до бази.