# make a class named Song that is-a object
class Song(object):
    # class Song has-a __init__ that takes self and lyrics parameters
    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print line

# set happy_bday to an instance of Song
happy_bday = Song(["Happy birthday to you",
                   "I don't want to get sued",
                   "So I'll stop right there"])

bulls_on_parade = Song(["They rally around tha family",
                        "With pockets full of shells"])

# from happy_bday get the function sing_me_a_song
happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()
