import sqlite3

db = sqlite3.connect('db.bin')

c = db.cursor()

def adding_a_playlist():
    add_name_playlist = str(input("Which playlist do you want to add?:"))
    c.execute('SELECT * FROM playlists')
    extracts_the_table_from_the_database = c.fetchall()
    if add_name_playlist != '':
        for i in range(len(extracts_the_table_from_the_database)):
            if add_name_playlist in extracts_the_table_from_the_database[i]:
                return "\nSuch a playlist exists\n"
        else: 
            c.execute('INSERT INTO playlists (playlist) VALUES ("{}")'.format(add_name_playlist))
    else:
        print("Error") 



        
                 
def delete_a_playlist():
    delete_name_playlist = str(input("Which playlist do you want to delete?:"))
    c.execute('SELECT * FROM playlists')
    extracts_the_table_from_the_database = c.fetchall()
    if delete_name_playlist != '':
        for i in range(len(extracts_the_table_from_the_database)):
            if delete_name_playlist in extracts_the_table_from_the_database[i]:
                delete_playlist = c.execute('DELETE FROM playlists WHERE playlist = "{}"'.format(delete_name_playlist))
                return delete_playlist
        else: 
            return "\nSuch a playlist exists\n"
    else:
        print("Error")
print(adding_a_playlist())
print(delete_a_playlist())

db.commit()
db.close()