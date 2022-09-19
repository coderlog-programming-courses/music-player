import sqlite3


def create_datebase():
    connection = sqlite3.connect('db.bin')
    cursor = connection.cursor()

    cursor.execute('CREATE TABLE playlists(id INTEGER PRIMARY KEY NOT NULL, playlist TEXT NOT NULL)')
    cursor.execute('CREATE TABLE connect(id_playlist INTEGER NOT NULL, id_music INTEGER NOT NULL)')
    cursor.execute('CREATE TABLE musics(id INTEGER PRIMARY KEY, music TEXT NOT NULL)')
    connection.commit()

    connection.close()
    
    
def adding_a_playlist_db(add_name_playlist):
    
    connection = sqlite3.connect('db.bin') # Підключення до бази даних (sqlite3)
    cursor = connection.cursor() # Робить курсор
    cursor.execute('INSERT INTO playlists (playlist) VALUES ("{}")'.format(add_name_playlist)) # Записує до бази даних (sqlite3) ім'я плейлиста
    connection.commit() # Зберігає те що ми записали
    cursor.close() # Закриває запис
    connection.close() # Відключяється від бази даних (sqlite3)
    
    
def delete_a_playlist_db(delete_id_playlist):
    
    connection = sqlite3.connect('db.bin') # Підключення до бази даних (sqlite3)
    cursor = connection.cursor() # Робить відкриття запису
    cursor.execute('DELETE FROM playlists WHERE id = "{}"'.format(delete_id_playlist)) # Видаляє з бази даних (sqlite3) плейлист по айді
    cursor.execute('SELECT * FROM connect WHERE id_playlist = "{}"'.format(delete_id_playlist)) # Вибірає айді плейлиста
    playlist_id = cursor.fetchall() # Виводить це в форматі текста
    for i in range(len(playlist_id)): # Проходиться по тому що ми взяли з таблиці
        cursor.execute('DELETE FROM musics WHERE id = "{}"'.format(playlist_id[i][1])) # Видаляє плейлист
    cursor.execute('DELETE FROM connect WHERE id_playlist = "{}"'.format(delete_id_playlist)) # Видаляє все що єсть в плейлисті
    connection.commit() # Записуе все до бази даних (sqlite3)
    cursor.close() # Закриває запис
    connection.close() # Закриває підключення до бази даних (sqlite3)
    
    
def renaming_the_playlist_db(id_playlist, new_name_playlist): # Робить функцію
    
    connection = sqlite3.connect('db.bin') # Підключається до бази даних (sqlite3)
    cursor = connection.cursor() # Відкриває курсор
    cursor.execute('UPDATE playlists SET playlist = "{}" WHERE id = "{}"'.format(new_name_playlist, id_playlist)) # Переіменовує плейлист
    connection.commit() # Записує в базу даних (sqlite3)
    cursor.close() # Закриває курсор
    connection.close() # Відключається від бази даних (sqlite3)