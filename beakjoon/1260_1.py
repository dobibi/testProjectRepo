import collections


from collections import deque
import queue

#BFS

def dfs(graph, start):
    visited[start] = True
    print(start, end='')
    for i in graph[start]:
        if not visited[i]:
            dfs(graph, i)

def bfs(graph, start):
    visited_bfs = [False] * (n+1)
    queue = deque([start])
    visited_bfs[start] = True
    
    while queue:
        x = queue.popleft()
        print(x, end='')
        for i in graph[x]:
            if not visited_bfs[i]: 
                queue.append(i)
                visited_bfs[i] = True

#main
n, m, v = map(int, input().split())
graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)

for _ in range(m):
    root, leaf = map(int, input().split())
    graph[root].append(leaf) # 무방향 그래프
    graph[leaf].append(root) # 서로 추가해준다
graph = [sorted(set(x)) for x in graph] # 중복 제거 후 오름차순 정렬
# Execute
dfs(graph, v)
print()
bfs(graph, v)