from pygame import mixer # Імпортує модуль mixer з бібліотеки pygame
from loguru import logger # Імпортує модуль logger з бібліотеки loguru


logger.add('logs/player.log', format='{time} {level} {message}', rotation="10MB") # Створення файлу logs/player.log де зберігається вся інформація про журнали(логи) 


def pause_music(): # Створення функціїї pause_music

        if mixer.music.pause(): # Використання модуля mixer з бібліотеки pygame для паузи запущеного аудіофайлу

                logger.info("That function(pause_music) is worked") # Журнал(лог) який повідомляє про успішне виконання функції pause_music 
        else:
                logger.error("That function(pause_music) did not woked!") # Журнал(лог) який повідомляє про  не успішне виконання функціїpause_music



def play_music(way): # Створення функціїї play_music яка приймає єдиний аргумент,id(айди аудіофайлу з бази даних sqlite3 таблиці musics)

        mixer.init() # Використання модуля mixer з бібліотеки pygame для створення репозиторію для аудіофайлу

        mixer.music.load("{}".format(way)) # Використання модуля mixer з бібліотеки pygame для загрузки обраного аудіофайлу до вже створеного вище репозиторію

        if mixer.music.play(): # Використання модуля mixer з бібліотеки pygame для запуску обраного аудіо файлуфайлу

           while True: # Цикл який постійно виконується,потрібно для то щоб аудіофайл міг програватися
                pass

                logger.info("That function(play_music) is worked") # Журнал(лог) який повідомляє про успішне виконання функції play_music
        else:
                logger.error("That function(play_music) did not worked! ") # Журнал(лог) який повідомляє про  не успішне виконання функції play_music



def rewind_music(second): # Створення функції rewind_music яка приймає єдиний аргумент,second(час на який' потрібно перемотати потрібно перемотати,записується в секундах)

     if mixer.music.set_pos(int("{}".format(second))): # Використання модуля mixer з бібліотеки pygame для перемотки обраного аудіофайлу на обрани час(секунду)

        logger.info(" That function(rewind_music) worked ") # Журнал(лог) який повідомляє про успішне виконання функції rewind_music
     else:
        logger.error(" That function(rewind_music) did not worked! ") # Журнал(лог) який повідомляє про  не успішне виконання функції rewind_music



def unpause_music(): # Створення функціїї unpause_music

        if mixer.music.unpause(): # Використання модуля mixer з бібліотеки pygame для відтворення аудіофайлу який був поствлений на паузу за допомогою функції pause_music

                logger.info(" That function(unpause_music) is worked ") # Журнал(лог) який повідомляє про успішне виконання функції unpause_music
        else:
                logger.error(" That function(unpause_music) did not worked! ") # Журнал(лог) який повідомляє про не успішне виконання функції unpause_music



def stop_music(): # Створення функції stop_music

        if mixer.music.stop(): # Використання модуля mixer з бібліотеки pygame для повного зупинення аудіофайлу тобто для вимкнення вибраного треку

                logger.info("That function(stop_music) is worked") # Журнал(лог) який повідомляє про успішне виконання функції stop_music
        else:
                logger.error("That function(stop_music) did not worked!") # Журнал(лог) який повідомляє про  не успішне виконання функції stop_music
