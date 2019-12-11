class Graph(object):
    def __init__(self, n):
        self.graph = [[0 for i in range(n)] for i in range(n)]

    def add_edge(self, i , j , w):
        self.graph[i][j] = w
    




