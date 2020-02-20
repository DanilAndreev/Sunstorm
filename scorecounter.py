import reader

class ScoreCounter:
    def __init__(self, libraries):
        self.libraries = libraries
        self.score = 0


    def count(self):
        repeated = []
        for library in self.libraries:
            for book in library.books:
                if book.ID not in repeated:
                    repeated.append(book.ID)
                    self.score += book.score
        return self.score


if __name__ == "__main__":
    file_content = reader.parse_from('a_example.txt')
    sc = ScoreCounter(file_content)
    print(sc.count())