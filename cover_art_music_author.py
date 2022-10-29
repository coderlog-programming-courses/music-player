from ast import If
import os
from db_worker import does_file_exist_db
from mutagen.mp3 import EasyMP3
import eyed3





def author_photo_name_music(way):
    # Робить функцію яка виводить обложку музики, ім'я автора та ім'я музики
    audiofile = eyed3.load(way)
    if None == audiofile.tag.artist:
        return ["Невідомий виконавець"]
    else:
        return [audiofile.tag.artist, audiofile.tag.title]
    
    
    

print(author_photo_name_music('/home/sasha/Музыка/Milana Star & Vitamin T - Сладкоежка.mp3'))
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
