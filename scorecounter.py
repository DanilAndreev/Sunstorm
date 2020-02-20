import sys

class ScoreCounter:
    def __init__(self, filename):
        self.filename = filename
        with open(filename, mode='r') as inp:
            self.count_of_lib = int(inp.readline())
            self.inp = inp
        self.score = 0


    def count(self):
        repeated = []
        with open(self.filename, mode='r') as inp:
            inp.readline()
            for i in range(self.count_of_lib):
                list_from_f_l = [int(token) for token in inp.readline().split(' ')]
                list_from_s_l = [int(token) for token in inp.readline().split(' ')]
                for j in range(int(list_from_f_l[1])):
                    if int(list_from_s_l[j]) not in repeated:
                        repeated.append(int(list_from_s_l[j]))
                        self.score += 1
        return self.score


if __name__ == "__main__":
    sc = ScoreCounter('input_set.txt')
    print(sc.count())