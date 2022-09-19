import sqlite3

def create_datebase():
    connection = sqlite3.connect('db.bin')
    cursor = connection.cursor()

    cursor.execute('CREATE TABLE playlists(id INTEGER PRIMARY KEY NOT NULL, playlist TEXT NOT NULL)')
    cursor.execute('CREATE TABLE connect(id_playlist INTEGER NOT NULL, id_music INTEGER NOT NULL)')
    cursor.execute('CREATE TABLE musics(id INTEGER PRIMARY KEY, music TEXT NOT NULL)')
    connection.commit()

    connection.close()

def add_music(path_to_music):#Оголошує функцію
    
    connection = sqlite3.connect('db.bin')#Підключення до бази даних
    cursor = connection.cursor()#Підключення до курсору 
    cursor.execute('INSERT INTO musics (music) VALUES ("{}")'.format(path_to_music))#Записує в таблицю musics(music) шлях до музики
    cursor.close()#Закриває курсор
    connection.commit()#Зберігає написане

    connection.close()#Закриває підключення

def delete_music(id):#Оголошує функцію

    connection = sqlite3.connect('db.bin')#Підключення до бази даних
    cursor = connection.cursor()#Підключення до курсору
    cursor.execute('DELETE FROM musics WHERE id = "{}"'.format(id))#Видаляє з таблиці musics id музики
    cursor.close()#Закриває курсор
    connection.commit()#Зберігає написане

    connection.close()#Закриває підключення