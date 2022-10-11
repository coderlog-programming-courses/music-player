from loguru import logger
import os



def author_photo_name_music(way):
    # Робить функцію яка виводить обложку музики, ім'я автора та ім'я музики

    music = os.path.basename(way)
    dash = music.find('-')
    music_author = music[:dash]
    music_name = music[dash + 2:]
    music_name = music_name.replace('.mp3', '').replace('-', '') 
    return (music_author, music_name)
