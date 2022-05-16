from collections import deque
import queue

n, m, v = map(int, input().split())
graph =[[] for _ in range(n+1)] # n+1개의 graph list 공간을 만듬(0번째  list는 1부터 시작하는 것을 유도하기 위해서 추가)

for i in range(m):
    temp_list = list(map(int,input().split())) #간선의 정보를 입력
    graph[temp_list[0]].append(temp_list[1])
    graph[temp_list[1]].append(temp_list[0])
    
for i in range(n+1) : # 작은 것을 먼저 방문 함으로
    graph[i].sort() # 각 간선의 정보에서 sorting

# DFS
def dfs(graph, v, visited):
    visited[v] = True
    print(v, end=' ')
    
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i , visited)


def bfs(graph, v, visited):
    quese = deque([start])
    
    visited[start] = True
    
    while quese:
        v = quese.popleft()
        print(v, end=' ')
        
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True


visited = [False]*(n+1) #방문 여부 표시
dfs(graph, v, visited)
print()
visited = [False]*(n+1)
bfs(graph, v, visited)

