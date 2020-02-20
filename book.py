

class Book:
    def __init__(self, score):
        self.score = int(score)
        self.references = []

    def add_reference(self, lib):
        self.references += [lib]

    def toString(self):
        return ""