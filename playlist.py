from db_worker import adding_playlist_db, delete_playlist_db, renaming_playlist_db, playlist_output_form_letter_db1, playlist_output_form_letter_db2, output_all_playlists # Імпортує функції з базами даних (sqlite3)
from loguru import logger # Імпортує бібліотеку з логами

logger.add("logs/player.log", format="{time} | {level} | {message}", rotation="10MB") # Додає файл куди зкладаються всі логи


def adding_playlist(add_name_playlist): # Робить функцію 
      
    if add_name_playlist == '': # Якщо строка пуста то... 
        logger.error("This function(adding_playlist) didn't worked ") # Добавляє лог який каже що функція не відпрацювала  
        return "Error" # ...помилка
    else: # Інакше
        adding_playlist_db(add_name_playlist) # Додаю функцію яка підключається до бази даних (sqlite3) 
        logger.info("This function(adding_playlist) worked ") # Добавляє лог який каже що функція відпрацювала  
        return "Add a playlist" # Каже що все добре та плейлист додався


def playlist_output_form_letter(id_playlist): # Робить функцію

    name_playlist_all_paths_music_list = [] # Робить пустий список у якому буде назва плейлиста потім уся музика та путь до неї яка єсть в плейлисті
    all_music = playlist_output_form_letter_db2(id_playlist)     
    name_playlist = playlist_output_form_letter_db1(id_playlist)   
    for i in range(len(name_playlist)):
        name_playlist = name_playlist[i][i]
    name_playlist_all_paths_music_list.append(name_playlist) # Додає всю музику в список        
    name_playlist_all_paths_music_list.append(all_music) # Додає у пустий список ім'я плейлиста і все що ми з ним зробили раніше

    logger.info("This function(playlist_output_form_letter) worked ") # Добавляє лог який каже що функція відпрацювала
    return name_playlist_all_paths_music_list # Виводить список в який ми додали дві змінні з текстом

print(playlist_output_form_letter(2))
