class Task:
    def __init__(self, books_num, libs_num, days):
        self.books_num = books_num
        self.libs_num = libs_num
        self.days = days


class Book:
    def __init__(self, ID, score):
        self.ID = ID
        self.score = score


class Library:
    def __init__(self, ID : int, books_num : int, signup_time : int, books_per_day : int, books):
        self.ID = ID
        self.books_num = books_num
        self.signup_time = signup_time
        self.books_per_day = books_per_day
        self.books = books

    def calc_books_score(self):
        return sum(book.score for book in self.books)

