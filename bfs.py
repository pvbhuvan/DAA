from collections import deque

n = int(input("Enter number of vertices: "))

graph = {}

for i in range(n):
    graph[i] = list(map(int, input(f"Enter neighbors of {i}: ").split()))

start = int(input("Enter starting vertex: "))

visited = set()
queue = deque([start])
visited.add(start)

print("BFS Traversal:", end=" ")

while queue:
    node = queue.popleft()
    print(node, end=" ")

    for neighbor in graph[node]:
        if neighbor not in visited:
            visited.add(neighbor)
            queue.append(neighbor)