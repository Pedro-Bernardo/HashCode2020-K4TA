from utils import *
from library import Library
from book import Book
# from Slideshow import Slideshow
import sys



def Main(input_path):
    with open(input_path, 'r') as file:
        lines = file.readlines()
    
    B, L, D = lines[0].split()
    B = int(B)
    L = int(L)
    D = int(D)
    books = []
    scores = lines[1].split()
    lines = lines[2:]

    libs = []

    for b in range(B):
        books.append(Book(scores[b]))

    for i in range(0, 2*L, 2):
        lib = Library(lines[i].split())
        lib.add_ids(lines[i+1].split())
        lib.calc_value(books)
        libs += [lib]


    
    

if __name__ == '__main__': 
    Main(sys.argv[1])