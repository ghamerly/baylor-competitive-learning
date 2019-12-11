

###graph class assumes weighted graphs
###graph stored in a matrix
size = 6
def BFS(graph, start):
    visited = [False]*len(graph)
    queue=[]
    queue.append(start)
    visited[start] = True
    while queue:
        start = queue.pop(0)
        for i in range(size):
            if graph[start][i] != 0 and visited[i] == False:
                queue.append(i)
                visited[i] = True


def DFS_recur(start, visited, graph):
    visited[start] = True
    for i in range(size):
        if graph[start][i] != 0 and visited[i] == False:
            DFS_recur(i, visited, graph)

def dfs(start, graph):
    visited = [False] * len(graph)
    DFS_recur(start,visited,graph)

