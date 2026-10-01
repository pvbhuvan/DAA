n = int(input("Enter number of vertices: "))
e = int(input("Enter number of edges: "))

graph = [[] for i in range(n)]

for i in range(e):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

start = int(input("Enter starting vertex: "))

visited = [False] * n

def dfs(node):
    visited[node] = True
    print(node, end=" ")

    for x in graph[node]:
        if not visited[x]:
            dfs(x)

dfs(start)