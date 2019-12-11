class disjoint_set(object):
    def __init__(self, n):
        self.pset = [i for i in range(n)]

    def find_set(self, n):
        if self.pset[n] != n:
            self.pset = self.find_set(n)

        return self.pset[n]

    def is_same_set(self, i, j):
        return self.find_set(i) == self.find_set(j)

    def union_set(self, i , j):
        self.pset[self.find_set(i)] = self.find_set(j)

    def count_sets(self):
        ret = 0
        for i in range(len(self.pset)):
            if self.pset[i] == i :
                ret += 1

        return ret
