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

    def total_score(self,books_to_send):
        total = 0
        limit = books_to_send
        i = 0
        while i < limit:
            if self.ids[i] < 0:
                i += 1
                limit += 1
                continue
            total += utils.books[self.ids[i]].score
            i +=1

        return total

    def add_ids(self, ids):
        self.ids = map(lambda x: int(x), ids)

    def calc_value(self,D,media_score,media_time,media_books):
        books_to_send=min((D-self.time)*self.books_p_day,self.n_books)
        self.value = self.total_score(books_to_send)-(self.time-media_time)*media_score*media_books*10

    def nullify(self, idx, book_id):
        # self.null_idx = max((self.null_idx - 1), 0)
        # self.ids[idx], self.ids[self.null_idx] = self.ids[self.null_idx], self.ids[idx]
        # del self.ids[idx]
        # self.ids.append(book_id)
        self.ids[idx] = -book_id
        self.n_books -= 1
        

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
        
    def select_books(self, limit):
        i = 0
        books_to_ret = []
        add_to = books_to_ret.append

        while i < limit:
            if self.ids[i] < 0:
                i += 1
                limit += 1
                continue
            add_to(self.ids[i])
            i +=1
        return books_to_ret

    def sort_books(self):
        self.ids.sort(reverse=True, key=lambda id: utils.books[id].score)
        for i in range(self.n_books):
            utils.books[self.ids[i]].add_reference((self.id, i)) 
