class Song:
    def __init__(self, name):
        self.name = name
        self.next = None

def next_song(self, song):
    self.next = song

def is_repeating_playlist(self):
    first = self.name
    def recursion(self,first):
        if self.next == None:
            return False

        while not first == self.next.next.name:
            recursion(self.next, first)
            break
        print('break out')
        return True

    return recursion(self,first)


first = Song("Hello")
second = Song("Eye of the tiger")
third = Song("mamma mia!")
fourth = Song("lion king")

first.next_song(second)
second.next_song(third)
third.next_song(fourth)
fourth.next_song(first)

print(first.is_repeating_playlist())