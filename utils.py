

def parseInput(path):
    photos = []
    lines = []

    with open(path, 'r') as file:
        lines = file.readlines()[1:]
    
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
    

    for l in lines:
        l = l[:-1]
        tokens = l.split(' ')
        photos.append([tokens[0], tokens[2:]])

    return photos


def output(outpath, slideshow):
    pass

def photoList(input_data):
    for i in range(len(input_data)):
        input_data[i] = [input_data[i][0], input_data[i][1][1]]

    return input_data


def orientationDic(photos):
    dic = {'H': [], 'V': []}

    for p in photos:
        dic[p[1][0]].append([p[0], p[1][1]])

    return dic


#[['H', ['cat', 'beach']],['V', ['cat', 'old people']]]