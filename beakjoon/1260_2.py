import sys
from collections import deque

n, m, v = map(int, sys.stdin.readline().split())

a_list = [[False]*(n+1) for i in range(n+1)]
visited = [False]*(n+1)


for i in range(m):
    a, b = map(int, sys.stdin.readline().split())
    a_list[a][b] = a_list[b][a] = True

print(visited)
print(a_list)


def dfs(x):
    if visited[x] == False :
        print(x, end='')
        
        for i in range(1, n+1):
            if a_list[x][i] == True:
                dfs(i)
                
def bfs(x):
    queue = deque([x])
    visited[x] = False
    
    while queue:
        x=queue.popleft()
        print(x, end="")                

        for i in range(1, n+1):
            if(visited[i]  == True and a_list[x][i] == True):
                visited[i] = False
                queue.append(i)

dfs(v)
print()
bfs(v)

