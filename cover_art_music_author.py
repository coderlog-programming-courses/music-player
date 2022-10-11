import os
from db_worker import does_file_exist_db, delete_music_db


def author_photo_name_music(way):
    # Робить функцію яка виводить обложку музики, ім'я автора та ім'я музики

    music = os.path.basename(way)
    dash = music.find('-')
    music_author = music[:dash]
    music_name = music[dash + 2:]
    music_name = music_name.replace('.mp3', '')
    return (music_author, music_name)
    
    
#print(author_photo_name_music('/home/sasha/Музика/Егор Крид feat. Филипп Киркоров - Цвет Настроения Чёрный.mp3'))
def does_file_exist():
    index = 0
    output_musics = does_file_exist_db()
    for i in range(len(output_musics)):
        way = os.path.relpath(output_musics[i][index], start=None)    
        s = os.path.exists(way) 
        if s != True:
            
            delete_music_db(s)
    index += 1

print(does_file_exist())
#'/home/sasha/Загрузки/Егор Крид feat. Филипп Киркоров - Цвет Настроения Чёрный.mp3'