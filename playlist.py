import sqlite3

def adding_a_playlist(add_name_playlist):
    if add_name_playlist == '':
        return "Error"
    else:     
        connection = sqlite3.connect('db.bin')
        cursor = connection.cursor()    
        cursor.execute('INSERT INTO playlists (playlist) VALUES ("{}")'.format(add_name_playlist))
        connection.commit()
        connection.close()
        return "Add a playlist"
         
def delete_a_playlist(delete_id_playlist):
    music_list = []
    connection = sqlite3.connect('db.bin')
    cursor = connection.cursor()
    cursor.execute('DELETE FROM playlists WHERE id = "{}"'.format(delete_id_playlist))
    cursor.execute('SELECT * FROM connect WHERE id_playlist = "{}"'.format(1))
    playlist_id = cursor.fetchall()
    for i in range(len(playlist_id)):
        cursor.execute('DELETE FROM musics WHERE id = "{}"'.format(playlist_id[i][1]))
    cursor.execute('DELETE FROM connect WHERE id_playlist = "{}"'.format(1))
    connection.commit()
    connection.close() 
