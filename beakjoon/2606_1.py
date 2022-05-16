#BFS

from collections import deque

n = int(input())
m = int(input())

graph = [[0]*(n+1) for _ in range(n+1)]

for _ in range(m):
    a,b = map(int, input().split())
    graph[a][b] = graph[b][a] =1
    
visited = [0]*(n+1)

def bfs(v):
    visited[v] = 1
    queue = deque()
    queue.append(v)
    while queue:
        node = queue.popleft()
        for i in range(n+1):
            if graph[i][node] == 1 and visited[i] == 0:
                queue.append(i)
                visited[i] = 1

bfs(1)
print(sum(visited)-1)

