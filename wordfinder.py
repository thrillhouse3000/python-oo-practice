from random import choice

class WordFinder:
    """Word Finder: finds random words from a dictionary.
    
    >>> wf = WordFinder("words.txt")
    235888 words read!

    >>> isinstance(wf, WordFinder)
    True

    >>> isinstance(wf.random(), str)
    True

    >>> sf = SpecialWordFinder("special_words.txt")
    4 words read!

    >>> isinstance(sf, WordFinder)
    True

    >>> isinstance(sf.random(), str)
    True
    """

    def __init__(self, path):
        self.path = path
        self.words = self.read_file
        print(f"{len(self.read_file())} words read!")
    
    def read_file(self):
        with open(self.path) as file:
            words = [line.strip() for line in file]
        return words

    def random(self):
        return choice(self.words())

class SpecialWordFinder(WordFinder):
    """Finds random words in a dictionary with special words"""

    def read_file(self):
        with open(self.path) as file:
            words = [line.strip() for line in file if line.strip() and not line[0] == '#']
        return words