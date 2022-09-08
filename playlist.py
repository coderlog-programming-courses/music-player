import sqlite3

def adding_a_playlist(add_name_playlist):
    connection = sqlite3.connect('db.bin')
    cursor = connection.cursor()    
    if add_name_playlist == '':
        return "Error"
    else: 
        cursor.execute('INSERT INTO playlists (playlist) VALUES ("{}")'.format(add_name_playlist))
        return "Add a playlist"
    connection.commit()
    connection.close()

          
def delete_a_playlist(delete_id_playlist):
    connection = sqlite3.connect('db.bin')
    cursor = connection.cursor()
    cursor.execute('DELETE FROM playlists WHERE id = "{}"'.format(delete_id_playlist))
    return "Delete playlist"
    connection.commit()
    connection.close()

print(adding_a_playlist(str(input("Add Playlist:"))))
print(delete_a_playlist(str(input("Delete Playlist:"))))