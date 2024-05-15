# For example, the following code prints "True" as both songs point to each other. why?
class Song:
    def __init__(self, name):
        self.name = name
        self.next = None

    def next_song(self, song):
        self.next = song

    def is_repeating_playlist(self):
        seen = list()
        node = self
        while node:
            if node in seen:
                return True
            else:
                seen.append(node)
                node = node.next
        return False


first = Song("Hello")
second = Song("Eye of the tiger")
first.next_song(second)
second.next_song(first)
assert first.is_repeating_playlist() is True


first = Song("Hello")
second = Song("Eye of the tiger")
third = Song("Brave New World")
first.next_song(second)
second.next_song(third)
assert first.is_repeating_playlist() is False
print('Tests passed.')
