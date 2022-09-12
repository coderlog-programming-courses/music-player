import sqlite3

def adding_a_playlist(add_name_playlist):
    if add_name_playlist == '':
        return "Error"
    else:     
        connection = sqlite3.connect('db.bin')
        cursor = connection.cursor()    
        cursor.execute('INSERT INTO playlists (playlist) VALUES ("{}")'.format(add_name_playlist))
        connection.commit()
        cursor.close()
        connection.close()
        return "Add a playlist"
         
def delete_a_playlist(delete_id_playlist):
    music_list = []
    connection = sqlite3.connect('db.bin')
    cursor = connection.cursor()
    cursor.execute('DELETE FROM playlists WHERE id = "{}"'.format(delete_id_playlist))
    cursor.execute('SELECT * FROM connect WHERE id_playlist = "{}"'.format(delete_id_playlist))
    playlist_id = cursor.fetchall()
    for i in range(len(playlist_id)):
        cursor.execute('DELETE FROM musics WHERE id = "{}"'.format(playlist_id[i][1]))
    cursor.execute('DELETE FROM connect WHERE id_playlist = "{}"'.format(delete_id_playlist))
    connection.commit()
    cursor.close()
    connection.close()

def playlist_output_in_the_form_of_a_letter(id_playlist):
    the_name_playlist_and_all_paths_music_list = []
    connection = sqlite3.connect('db.bin')
    cursor = connection.cursor()
    cursor.execute('SELECT playlist FROM playlists WHERE id = "{}"'.format(id_playlist))
    name_playlist = cursor.fetchall()
    name_playlist = str(name_playlist) 
    name_playlist = name_playlist.replace("(", "")
    name_playlist = name_playlist.replace(")","")
    name_playlist = name_playlist.replace("]", "")
    name_playlist = name_playlist.replace("[", "") 
    name_playlist = name_playlist.replace(",", "")   
    cursor.execute("""SELECT id, music FROM musics, connect WHERE id_playlist = "{}" AND id = id_music""".format(id_playlist))
    all_music = cursor.fetchall()
    all_music = str(all_music)
    all_music = all_music.replace("]", "")
    all_music = all_music.replace("[", "") 
    the_name_playlist_and_all_paths_music_list.append(name_playlist)
    the_name_playlist_and_all_paths_music_list.append(all_music)
    the_name_playlist_and_all_paths_music_list = str(the_name_playlist_and_all_paths_music_list)
    the_name_playlist_and_all_paths_music_list = the_name_playlist_and_all_paths_music_list.replace("'", "")
    the_name_playlist_and_all_paths_music_list = the_name_playlist_and_all_paths_music_list.replace('"', '')
    connection.commit()
    cursor.close()
    connection.close() 
    return the_name_playlist_and_all_paths_music_list


def renaming_the_playlist(id_playlist, new_name_playlist):
    connection = sqlite3.connect('db.bin')
    cursor = connection.cursor()    
    cursor.execute('UPDATE playlists SET playlist = "{}" WHERE id = "{}"'.format(new_name_playlist, id_playlist))
    connection.commit()
    cursor.close()
    connection.close()
