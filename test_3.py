from task_3 import Song, Album

song_1 = Song('Shape of you', 'Ed Sheeran', '2013', 10)
song_2 = Song('Castle on the Hill', 'Ed Sheeran', '2013', 10)
song_3 = Song('Thinking Out Loud', 'Ed Sheeran', '2013', 15)
song_4 = Song('Photograph', 'Ed Sheeran', '2013', 15)
album_1 = Album("Autumn Variations", [song_1, song_2, song_3, song_4])
album_2 = Album("No.6 Collaborations", [song_4, song_3, song_2, song_1])


def menu():
    print('Albums:')
    for number, album_name in enumerate(Album.all_albums, start=1):
        print(f'{number}. {album_name}')
    choice_1 = int(input('Select the album you want to listen to: '))
    choice_album_name = list(Album.all_albums.keys())[choice_1 - 1]
    selected_album = Album.all_albums[choice_album_name]

    print('')
    print('Songs in the album:')
    for number, song in enumerate(selected_album.songs, start=1):
        print(f'{number}. {song.name} by {song.artist} ({song.year_release})')

    choice_2 = int(input('Select the song you want to listen to from the list: '))
    choice_song = selected_album.songs[choice_2 - 1]

    start = int(input("Actions: \n"
                      "To start playing a song, enter - 1\n"
                      "To finish playing songs, press - 2\n"))
    if start == 1:
        selected_album.switch(choice_song)


menu()
