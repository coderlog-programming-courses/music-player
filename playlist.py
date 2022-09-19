from db_worker import adding_a_playlist_db, delete_a_playlist_db, renaming_the_playlist_db
import sqlite3

def adding_a_playlist(add_name_playlist): # Робить функцію 

    if add_name_playlist == '': # Якщо строка пуста то... 
        return "Error" # ...помилка
    else: # Інакше
        adding_a_playlist_db(add_name_playlist) # Додаю функцію яка підключається до бази даних (sqlite3) 
        return "Add a playlist" # Каже що все добре та плейлист додався
         

def playlist_output_in_the_form_of_a_letter(id_playlist): # Робить функцію

    the_name_playlist_and_all_paths_music_list = [] # Робить пустий список у якому буде назва плейлиста потім уся музика та путь до неї яка єсть в плейлисті
    connection = sqlite3.connect('db.bin') # Підключення до бази даних (sqlite3)
    cursor = connection.cursor() # Робить курсор
    cursor.execute('SELECT playlist FROM playlists WHERE id = "{}"'.format(id_playlist)) # З таблиці плейлист бере задане айді
    name_playlist = cursor.fetchall() # Бере те що ми взяли з бази даних (sqlite3) та робить його в змінну
    name_playlist = str(name_playlist) # Робить з 'name_playlist' строку
    name_playlist = name_playlist.replace("(", "").replace(")","").replace("]", "").replace("[", "").replace(",", "")   # Видаляє з зміної яку ми взяли з бази даних (sqlite3) все непотрібне 
    cursor.execute("""SELECT id, music FROM musics, connect WHERE id_playlist = "{}" AND id = id_music""".format(id_playlist)) # Бере із двох таблиць айді плейлистов та айді яке дорівнює айді музик з плейлиста
    all_music = cursor.fetchall() # Бере те що ми взяли з бази даних (sqlite3) та робить його в змінну
    all_music = str(all_music) # Робить із зміної 'all_music' строку
    all_music = all_music.replace("]", "").replace("[", "")  # Видаляє все непотрібне
    the_name_playlist_and_all_paths_music_list.append(name_playlist) # Додає у пустий список ім'я плейлиста і все що ми з ним зробили раніше
    the_name_playlist_and_all_paths_music_list.append(all_music) # Додає всю музику в список
    the_name_playlist_and_all_paths_music_list = str(the_name_playlist_and_all_paths_music_list) # Конвертує список у строку
    the_name_playlist_and_all_paths_music_list = the_name_playlist_and_all_paths_music_list.replace("'", "").replace('"', '') # Видаляє все непотрібне
    connection.commit() # Записує все до бази даних (sqlite3)
    cursor.close() # Закриває курсор
    connection.close() # Відключаєтьсяч від бази даних (sqlite3)
    return the_name_playlist_and_all_paths_music_list # Виводить список в який ми додали дві змінні з текстом

renaming_the_playlist_db() # Додає функцію з бази даних (sqlite3) 
delete_a_playlist_db() # Додає функцію з бази даних (sqlite3) 