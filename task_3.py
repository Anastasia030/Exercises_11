import time


class Song:
    """
    The class of the song from the album
    """

    def __init__(self, name, artist, year_release, time):
        """
        Initializes a Song object with the given attributes.
        :param name: str, the name of the song.
        :param artist: str, the artist of the song.
        :param year_release: str, the year of release of the song.
        :param time: int, the duration of the song in seconds.
        """
        self.name = name
        self.artist = artist
        self.year_release = year_release
        self.time = time
        self.play = False
        self.pause = False
        self.start_time = 0
        self.paused_time = 0

    def player(self):
        """
        Plays the song.
        """
        self.play = True
        self.pause = False
        self.start_time = time.time() - self.paused_time
        print(f'A song is playing now: {self.name} by {self.artist} ({self.year_release})')
        while time.time() - self.start_time < self.time:
            if (time.time() - self.start_time) % 2 == 0:
                if input('Would you like to pause the song? (Press Enter to continue): '):
                    self.pause = True
                    print(f'The song has been paused: {self.name} by {self.artist}')
                    while self.pause:
                        time.sleep(1)
                        if input('Press something to continue playing: '):
                            self.pause = False
                            print(f'The song has resumed playing: {self.name} by {self.artist}')
                            self.start_time += time.time() - self.start_time - self.paused_time
        print(f'The song has finished playing: {self.name} by {self.artist}')


class Album:
    """
    The artist's album class
    """
    all_albums = {}

    def __init__(self, name, songs):
        """
        Initializes an Album object with the given attributes.
        :param name: str, the name of the album.
        :param songs: str, a list of Song objects representing the songs on the album.
        """
        self.name = name
        self.songs = songs
        Album.all_albums[self.name] = self

    def switch(self, now):
        """
        Plays the songs on the album starting from the given song.
        :param now: str, the Song object representing the starting song.
        """
        index = self.songs.index(now)
        while index < len(self.songs):
            self.songs[index].player()
            index += 1
            if index < len(self.songs):
                print('\nPlaying next song...\n')
        print('\nAlbum finished.')
