import os.path
from db_worker import create_datebase


if os.path.exists('db.bin') != True: #Якщо файлу бази данних немає у папці
    create_datebase() #Запустить функцію, що створить його.
