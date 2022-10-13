import os
from db_worker import does_file_exist_db
from mutagen.mp3 import EasyMP3


def author_photo_name_music(way):
    # Робить функцію яка виводить обложку музики, ім'я автора та ім'я музики
    audio_list = []
    audio = EasyMP3(way)
    audio = [audio.tags]
    for i in range(len(audio)):
        name_music = audio[i]['title'][i]
        artist_music = audio[i]['artist'][i]
        audio_list.append(name_music)
        audio_list.append(artist_music)
    return audio_list


def does_file_exist():
    # Робить функцію яка виводить список музик якіх не існує
    absent_music = []
    output_musics = does_file_exist_db()    
    index = 0
    for i in range(len(output_musics)):
        way = os.path.relpath(output_musics[i][index], start=None)    
        if os.path.exists(way) != True:
            absent_music.append(output_musics[i][index])
    index += 1
    return absent_music
