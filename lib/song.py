
class Song:
    
    count = 0
    genres = []
    artists = []
    genre_count = {}
    artist_count = {}
    
    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre
        Song.add_song_to_count()
        Song.genres.append(self.genre)
        Song.artists.append(self.artist)
        
        Song.add_to_genres()
        Song.add_to_artists()
        Song.add_to_genre_count()
        Song.add_to_artist_count()


    @classmethod
    def add_song_to_count(cls):
        cls.count += 1

    @classmethod
    def add_to_genres(cls):
        cls.genres = list(dict.fromkeys(cls.genres))
        print('genres:', cls.genres)
         
    @classmethod
    def add_to_artists(cls):
        cls.artists = list(set(cls.artists))
        print('artists:', cls.artists)

    @classmethod
    def add_to_genre_count(cls):
            for genre in cls.genres:
                cls.genre_count[genre] = cls.genre_count.get(genre, 0) + 1
            print('genre count:', cls.genre_count)

    @classmethod
    def add_to_artist_count(cls):
        for artist in cls.artists:
            cls.artist_count[artist] = cls.artist_count.get(artist, 0) + 1
        print('artist count:', cls.artist_count)

Song("99 Problems", "Jay Z", "Rap")
Song("Halo", "Beyonce", "Pop")
Song("Smells Like Teen Spirit", "Nirvana", "Rock")
            



    
    


