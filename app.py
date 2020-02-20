from utils import *
from library import Library
from book import Book
import utils
# from Slideshow import Slideshow
import sys

utils.books = []

def Main(input_path):
    with open(input_path, 'r') as file:
        lines = file.readlines()
    
    B, L, D = lines[0].split()
    B = int(B)
    L = int(L)
    D = int(D)
    
    scores = lines[1].split()
    lines = lines[2:]

    libs = []

    for b in range(B):
        utils.books.append(Book(scores[b]))

    n_libs = 0
    for i in range(0, 2*L, 2):
        lib = Library(lines[i].split() + [i/2])
        lib.add_ids(lines[i+1].split())
        lib.calc_value()
        lib.sort_books()
        libs += [lib]
        n_libs += 1


    libs.sort(reverse=True, key=lambda lib: lib.value)
    final_libs = []
    len_final = 0

    i = 0
    while D > 0 and i < n_libs:
        lib = libs[i]
        # optimize
        if lib.time < D:
            books_to_send = min((D - lib.time)*lib.books_p_day, lib.n_books)
        else:
            i += 1
            continue

        final_libs += [{"ship_books": books_to_send, "id": lib.id, "books": lib.ids[:books_to_send]}]

        # update books score already sent to zero
        for book_id in lib.ids[:books_to_send]:
            utils.books[book_id].score = 0


        D = D - lib.time
        i += 1
        len_final += 1

    print utils.output(final_libs, len_final)



if __name__ == '__main__': 
    Main(sys.argv[1])