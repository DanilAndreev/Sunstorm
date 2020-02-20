import classes


def parse_from(filename):
    with open(filename) as fin:
        input = fin.readlines()
    books_count, libs_count, max_days = (int(i) for i in input[0].split(" "))
    books_scores = (int(i) for i in input[1].split(" \n"))
    libs = []
    for i in range(libs_count):
        lib_books_count, signup_time, books_ship_count = (int(i) for i in input[2 + i * 2].split(" "))
        lib_books = [int(i) for i in input[3 + i * 2].split(" ")]
        libs.append(classes.Library(i, lib_books_count, signup_time, books_ship_count, lib_books))
    return libs


if __name__ == "__main__":
    libs = parse_from("datasets/a_example.txt")
    print(libs[0].books_per_day)
