import os.path
<<<<<<< HEAD
from playlist import adding_a_playlist, delete_a_playlist, playlist_output_in_the_form_of_a_letter


=======
from db_worker import create_datebase
>>>>>>> origin


if os.path.exists('db.bin') != True:
<<<<<<< HEAD
    datebase()
=======
    create_datebase()
>>>>>>> origin
