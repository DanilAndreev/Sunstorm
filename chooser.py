import classes as classes


class Multipliers:
    def __init__(self, books_number, signup_time, getting_speed):
        self.books_number = books_number
        self.signup_time = signup_time
        self.getting_speed = getting_speed


is_first = True


def calc_priority(books_number: int, signup_time: int, getting_speed: int, multipliers: Multipliers):
    return books_number*multipliers.books_number + signup_time*multipliers.signup_time \
           + getting_speed*multipliers.getting_speed


def get_next_lib(libraries: list):
    global is_first
    if is_first:
        is_first = False
        return max(libraries,
                   key=lambda library: calc_priority(library.books_num, library.signup_time, library.books_per_day))
    else:
        return max(libraries,
                   key=lambda library: calc_priority(library.books_num, library.signup_time, library.books_per_day) and
                        True
                   )

