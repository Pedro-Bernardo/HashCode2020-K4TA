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
        libs += [lib]
        lib.sort_books()
        n_libs += 1

    final_libs = []
    len_final = 0

    lib_ids = range(n_libs)

    while D > 0:
        if not lib_ids:
            break
        media_score=0
        
        for b in utils.books:
            media_score+=b.score
        media_score=media_score/B
        media_time=0
        media_books=0
        c=0
        for lib in libs:
            media_time+=lib.time
            media_books+=lib.books_p_day
            c+=1
        media_books=media_books/c
        media_time=media_time/c
        for lib in libs:
            lib.sort_books()
            lib.calc_value(D,media_score,media_time,media_books)
        libs.sort(reverse=True, key=lambda lib: lib.value)
        while libs and libs[0].time>=D:
            libs=libs[1:]
        if not libs:
            break
        lib=libs[lib_ids[0]]
        lib_ids=lib_ids[1:]
        books_to_send = min((D - lib.time)*lib.books_p_day, lib.n_books)
        final_libs += [{"ship_books": books_to_send, "id": lib.id, "books": lib.select_books(books_to_send)}]

        # update books score already sent to zero
        for book_id in lib.ids[:books_to_send]:
            utils.books[book_id].score = 0
            for ref in utils.books[book_id].references:
                libs[ref[0]].nullify(ref[1],book_id)

        D = D - lib.time
        len_final += 1

    print utils.output(final_libs, len_final)



if __name__ == '__main__': 
    Main(sys.argv[1])