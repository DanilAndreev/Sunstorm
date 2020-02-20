def parse_from(filename):
    with open(filename) as fin:
        books_count, libs_count, max_days = (int(i) for i in fin.readline().split(" "))
    books_scores = (int(i) for i in fin.readline().split(" "))


if __name__ == "__main__":
    parse_from("a_example.txt")
