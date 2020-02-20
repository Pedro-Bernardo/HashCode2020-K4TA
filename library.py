class Library:
    def __init__(self, parameters):
        self.id = parameters[3]
        self.n_books = parameters[0]
        # time in days 0 -> D-1
        self.time = parameters[1]
        self.books_p_day = parameters[2]
        self.ids = []
        self.value = 0

    def total_score(self, B):
        total = 0
        for i in ids:
            total += B[i].get_score()
        return total

    def add_ids(self, ids):
        self.ids = ids

    def calc_value(self, B):
        self.value = (total_score(B)/n_books)*books_p_day

    def sort_books(self):
        self.ids.sort(reverse=True, key=self.comparator)

    def comparator(id):
        return books[id].score

    # D - signup
