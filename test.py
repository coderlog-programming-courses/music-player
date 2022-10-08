from pygame import *
from mutagen.mp3 import MP3


def set_pos(second):
    mixer.music.set_pos(int("{}".format(second)))
    set_pos()