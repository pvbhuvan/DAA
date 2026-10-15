import heapq

n = int(input())
e = int(input())

graph = [[] for _ in range(n)]

for _ in range(e):
    u, v, w = map(int, input().split())
    graph[u].append((w, v))
    graph[v].append((w, u))

visited = [False] * n
min_heap = [(0, 0, -1)]
mst_weight = 0
mst_edges = []

while min_heap and len(mst_edges) < n - 1:
    weight, u, parent = heapq.heappop(min_heap)

    if visited[u]:
        continue

    visited[u] = True
    mst_weight += weight

    if parent != -1:
        mst_edges.append((parent, u, weight))

    for w, v in graph[u]:
        if not visited[v]:
            heapq.heappush(min_heap, (w, v, u))

if n == 0 or len(mst_edges) != n - 1:
    print("MST does not exist")
else:
    for u, v, w in mst_edges:
        print(u, v, w)

    print(mst_weight)