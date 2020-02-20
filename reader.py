import classes


def parse_from(filename):
    with open(filename) as fin:
        input_str = fin.readlines()
    books_count, libs_count, max_days = (int(i) for i in input_str[0].split(" "))
    books_scores = [int(i) for i in input_str[1].split(" ")]
    libs_list = []
    for i in range(libs_count):
        lib_books_count, signup_time, books_ship_count = (int(i) for i in input_str[2 + i * 2].split(" "))
        lib_books = [classes.Book(int(i), books_scores[int(i)]) for i in input_str[3 + i * 2].split(" ")]
        libs_list.append(classes.Library(i, lib_books_count, signup_time, books_ship_count, lib_books))
    return libs_list


if __name__ == "__main__":
    libs = parse_from("datasets/a_example.txt")
    print([libs[0].books[i].score for i in range(5)])
