from chooser import Multipliers
import random


class Result:
    def __init__(self, score, multipliers):
        self.score = score
        self.multipliers = multipliers


def get_rnd_multipliers():
    total = 1000

    k1 = random.randint(1, total)
    k2 = random.randint(k1, total)
    k3 = total - k1 - k2

    return Multipliers(k1 / total, k2 / total, k3 / total)


results = []

for i in range(100):
    multipliers = get_rnd_multipliers()
    print(multipliers.books_number, multipliers.signup_time, multipliers.getting_speed, multipliers.books_number + multipliers.signup_time + multipliers.getting_speed)

results.sort(key=lambda x: x.score, reverse=True)

# print(results[0])
# print(results[:-1])
