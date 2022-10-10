import sqlite3 # Імпортує бібліотеку з базой даних (sqlite3)
from loguru import logger # Імпортує бібліотеку з логами

logger.add("logs/player.log", format="{time} | {level} | {message}", rotation="10MB") # Додає файл куди зкладаються всі логи



def create_datebase():
    connection = sqlite3.connect('db.bin')
    cursor = connection.cursor()

    #Створити таблицю playlistsю
    cursor.execute('CREATE TABLE playlists(id INTEGER PRIMARY KEY NOT NULL, playlist TEXT NOT NULL)')
    #Створити таблицю connect.
    cursor.execute('CREATE TABLE connect(id_playlist INTEGER NOT NULL, id_music INTEGER NOT NULL)')
    #Створити таблицю musics.
    cursor.execute('CREATE TABLE musics(id INTEGER PRIMARY KEY, music TEXT NOT NULL)')
    cursor.execute('INSERT INTO playlists (playlist) VALUES ("main")')
    connection.commit() #Затвердити зміни у бд.

    cursor.close() #Закртити курсос.
    connection.close() #Закрити підключення до бази.
    connection.close()
    
   
def adding_playlist_db(add_name_playlist): # Робить функцію
    
    connection = sqlite3.connect('db.bin') # Підключення до бази даних (sqlite3)
    cursor = connection.cursor() # Робить курсор  
      
    cursor.execute('INSERT INTO playlists (playlist) VALUES ("{}")'.format(add_name_playlist)) # Записує до бази даних (sqlite3) ім'я плейлиста
    connection.commit() # Зберігає те що ми записали    
    
    cursor.close() # Закриває запис
    connection.close() # Відключяється від бази даних (sqlite3)
    
    logger.info("This function(adding_playlist_db) worked ") # Добавляє лог який каже що функція відпрацювала
    
    
def delete_playlist_db(delete_id_playlist):
    
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
    
    logger.info("This function(delete_playlist_db) worked ") # Добавляє лог який каже що функція відпрацювала
    
   
def playlist_output_form_letter_db1(id_playlist): # Робить функцію
    
    connection = sqlite3.connect('db.bin') # Підключення до бази даних (sqlite3)
    cursor = connection.cursor() # Робить курсор
    
    cursor.execute('SELECT playlist FROM playlists WHERE id = "{}"'.format(id_playlist)) # З таблиці плейлист бере задане айді
    name_playlist = cursor.fetchall() # Бере те що ми взяли з бази даних (sqlite3) та робить його в змінну
    connection.commit() # Записує все до бази даних (sqlite3)
    
    cursor.close() # Закриває курсор
    connection.close() # Відключаєтьсяч від бази даних (sqlite3)
    
    logger.info("This function(playlist_output_form_letter_db1) worked ") # Добавляє лог який каже що функція відпрацювала
    name_playlist = list(name_playlist)
    return name_playlist

   
def playlist_output_form_letter_db2(id_playlist): # Робить функцію
    
    connection = sqlite3.connect('db.bin') # Підключення до бази даних (sqlite3)
    cursor = connection.cursor() # Робить курсор
    
    cursor.execute("""SELECT id, music FROM musics, connect WHERE id_playlist = "{}" AND id = id_music""".format(id_playlist)) # Бере із двох таблиць айді плейлистов та айді яке дорівнює айді музик з плейлиста
    all_music = cursor.fetchall() # Бере те що ми взяли з бази даних (sqlite3) та робить його в змінну
    connection.commit() # Записує все до бази даних (sqlite3)
    
    cursor.close() # Закриває курсор
    connection.close() # Відключаєтьсяч від бази даних (sqlite3)
    
    logger.info("This function(playlist_output_form_letter_db2) worked ") # Добавляє лог який каже що функція відпрацювала
    all_music = list(all_music)
    return all_music

   
def renaming_playlist_db(id_playlist, new_name_playlist): # Робить функцію
    
    connection = sqlite3.connect('db.bin') # Підключається до бази даних (sqlite3)
    cursor = connection.cursor() # Відкриває курсор
    
    cursor.execute('UPDATE playlists SET playlist = "{}" WHERE id = "{}"'.format(new_name_playlist, id_playlist)) # Переіменовує плейлист
    connection.commit() # Записує в базу даних (sqlite3)
    
    cursor.close() # Закриває курсор
    connection.close() # Відключається від бази даних (sqlite3)
    
    logger.info("This function(renaming_playlist_db) worked ") # Добавляє лог який каже що функція відпрацювала
    
   
def output_all_playlists(): # Робить функцію 
    
    connection = sqlite3.connect('db.bin') # Підключається до бази даних (sqlite3)
    cursor = connection.cursor() # Відкриває курсор
    
    cursor.execute('SELECT * FROM playlists') # Бере всі плейлисти з таблиці та виводить
    output_playlist = cursor.fetchall() # Записує в зміну те що ми взяли з бази даних (sqlite3)
    
    cursor.close() # Закриває курсор
    connection.close() # Відключається від бази даних (sqlite3)
    
    logger.info("This function(output_of_all_playlists) worked ") # Добавляє лог який каже що функція відпрацювала
    
    return output_playlist # Виводить зміну output_playlist в якій те що ми взяли з бази даних (sqlite3)

