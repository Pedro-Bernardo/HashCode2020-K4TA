import utils

class Library:
    def __init__(self, parameters):
        self.id = int(parameters[3])
        self.n_books = int(parameters[0])
        # time in days 0 -> D-1
        self.time = int(parameters[1])
        self.books_p_day = int(parameters[2])
        self.ids = []
        self.value = 0

    def total_score(self, B):
        total = 0
        for i in self.ids:
            total += B[i].score
        return total

    def add_ids(self, ids):
        self.ids = map(lambda x: int(x), ids)

    def calc_value(self):
        self.value = (self.total_score(utils.books)/self.n_books)*self.books_p_day

    # def toString(self):
    #     ship_books = len(self.ids)

    #     # assume self.ids eh os ids dos livros para dar ship
    #     output = "{} {}\n".format(str(self.id), ship_books)
        
    #     #print book ids that will be shipped
    #     for idx, id in enumerate(self.ids):
    #         output += str(id)
    #         if idx != ship_books - 1:
    #             output += " "
        
    #     output += "\n"

    #     return output
        
    def sort_books(self):
        self.ids.sort(reverse=True, key=lambda id: utils.books[id].score)


    # D - signup
