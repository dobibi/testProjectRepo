from collections import deque
import queue
import sys
input = sys.stdin.readline

def dfs(edges, v, visited):
    visited[v] = True
    print(v, end='')
    
    for e in edges[v]:
        if not visited[e] :
            dfs(edges, e, visited)
            
def bfs(edges, v, visited):
    queue = deque([v])
    visited[v] = True
    
    while queue:
        now = queue.popleft()
        print(now, end='')
        
        for e in edges[now]:
            if not visited[e]:
                queue.append(e)
                visited[e] = True
                
if __name__ =='__main__':
    n, m, v = map(int, input().split())
    edges = [[] for _ in range(n + 1)]
    
    for _ in range(m):
        a, b = map(int, input().split())
        edges[a].append(b)
        edges[b].append(a)
        
    for i in range(1, n + 1):
        edges[i].sort()
    
    visited = [False] * (n + 1)
    dfs(edges, v, visited)
    print()
    visited = [False] * (n + 1)
    bfs(edges, v, visited)        