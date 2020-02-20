class Library:
    def __init__(self, books, time, books_day):
        self.books = books
        # time in days 0 -> D-1
        self.time = time
        self.books_p_day = books_day
