import os.path
from db_worker import create_datebase


if os.path.exists('db.bin') != True:
    create_datebase()