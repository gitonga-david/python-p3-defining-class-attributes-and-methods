# instance attributes - responsible for holding information regarding an instance
# class attributes - responsible for holding information of entire class - has class scope
# class constants - responsible for holding information that doesn't change
class Album:

    # Class attributes
    album_count = 0

    # Class constant
    GENRE = ["Hip-Hop", "Pop", "Jazz"]

    def __init__(self, genre, date):
        if self.check_genre(genre):
            self.increase_album_count()
            self.genre = genre
            self.release_date = date

    @classmethod
    def check_genre(cls, genre):
        return genre in cls.GENRES

    @classmethod
    def increase_album_count(cls, increment=1):
        cls.album_count += increment
