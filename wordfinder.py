"""Word Finder: finds random words from a dictionary."""

import random
class WordFinder:
    """
    Function to find words in a file
    """
    
    def __init__(self, file):
        file_to_parse = open(file)
        self.words = self.parse(file_to_parse)
        print(f"{len(self.words)} read")

    def parse(self, file_to_parse):
        return [word.strip() for word in file_to_parse]
    
    def random(self):
        return random.choice(self.words)

class SpecialWordFinder(WordFinder):
    """
    Word finder that ignores blank spaces and lines that start with '#' in a list
    """

    def parse(self, file_to_parse):
        return [word.strip() for word in file_to_parse if word.strip() and not word.startswith('#')]