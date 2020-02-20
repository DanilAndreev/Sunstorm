import classes as classes


class Multipliers:
    def __init__(self, books_number, signup_time, getting_speed):
        self.books_number = books_number
        self.signup_time = signup_time
        self.getting_speed = getting_speed

    def __str__(self):
        return "" + str(self.books_number) + " " + str(self.signup_time) + " " + str(self.getting_speed)

is_first = True


def calc_priority(books_number: int, signup_time: int, getting_speed: int, multipliers: Multipliers):
    return books_number*multipliers.books_number + signup_time*multipliers.signup_time \
           + getting_speed*multipliers.getting_speed


def get_next_lib(libraries: list, chosen_libraries: list, multipliers_simple: Multipliers, multipliers_deep: tuple):
    global is_first
    if is_first:
        is_first = False
        result = max(libraries,
                   key=lambda library: calc_priority(library.books_num, library.signup_time,
                                                     library.books_per_day, multipliers_simple))
        libraries.remove(result)
        return result
    else:

        result = max(libraries,
                   key=lambda library: calc_priority(library.books_num, library.signup_time,
                                                     library.books_per_day, multipliers_simple) * multipliers_deep[0] +
                    sum([x.score for x in set([book for book in library.books for library in chosen_libraries]) ^ set(library.books)])
                   )
        libraries.remove(result)
        return result


def calculate_libs_order(libraries: list, multipliers_simple: Multipliers, multipliers_deep: tuple):
    result = []
    temp_libraries = libraries.copy()
    while len(temp_libraries) > 0:
        result.append(get_next_lib(temp_libraries, result, multipliers_simple, multipliers_deep))
    return result

