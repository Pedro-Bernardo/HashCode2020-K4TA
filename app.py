from utils import *
# from Slide import Slide
# from Slideshow import Slideshow
import sys



def Main(input_path):
    with open(input_path, 'r') as file:
        lines = file.readlines()
    
    B = int(l[0])
    L = int(l[1])
    D = int(l[2])
    scores = lines[3].split()

    lines = lines[4:]

    libs = []

    for i in range(0, 2*L, 2):
        lib = Library(line[i].split())
        lib.add_ids(line[i+1].split())
        libs.insert(lib, 0)

    

    

if __name__ == '__main__': 
    Main(sys.argv[1])