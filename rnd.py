from chooser import *
import random

from scorecounter import ScoreCounter


class Result:
    def __init__(self, score, multipliers: Multipliers):
        self.score = score
        self.multipliers = multipliers

    def __str__(self):
        return "" + str(self.score) + " : " + str(self.multipliers)


def get_rnd_multipliers():
    total = 1000

    k1 = random.randint(1, total)
    k2 = random.randint(1, total - k1)
    k3 = total - k1 - k2

    return Multipliers(k1 / total, k2 / total, k3 / total)


def print_rnd(libs):
    results = []

    for i in range(100):
        multipliers = get_rnd_multipliers()
        rnd_libs = calculate_libs_order(libs, multipliers, (0.5, 0.5))
        score = ScoreCounter(rnd_libs)
        score = score.count()
        result = Result(score, multipliers)
        results.append(result)
        print(result)

    results.sort(key=lambda x: x.score, reverse=True)

    print('')
    print(results[0])
    print(results[-1])

