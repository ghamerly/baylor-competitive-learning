import Data_structures.UnionFind as unionFind

import Point.Point as P

from math import sqrt, pow
def dis(a,b):
    return sqrt(pow((b.x - a.x), 2.0) + pow((b.y - a.y), 2.0))
test_cases = int(input())

a = []
for i in range(test_cases):
    c, d  = input().split()
    c = int(c)
    d = float(d)

    disjoint_set = unionFind.disjoint_set(c)

    for j in range(c):
        x , y = [float(k) for k in input().split()]
        a.append(P.Point(x,y))

    for k in range(c):
        for l in range(k+1, c):
            if dis(a[k], a[l]) <= d:
                disjoint_set.union_set(k,l)

    print(disjoint_set.count_sets())