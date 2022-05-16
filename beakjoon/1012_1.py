import sys
sys.setrecursionlimit(100000) # 재귀 최대깊이 지정

def dfs(x, y):
    if x < 0 or y < 0 or x >= row or y >=col or graph[x][y] !=1:
        return
    
    graph[x][y] = "x" # 배추있는 방문한 땅 x로 마킹
    dfs(x-1, y)
    dfs(x, y-1)
    dfs(x+1, y)
    dfs(x, y+1)
    
for i in range(int(input())):
       graph = list()
       count = 0
       row, col, k = map(int, input().split())
       graph = [[0 for i in range(col)] for x in range(row)]
       
       for _ in range(k):
           r, c = map(int, input().split())
           graph[r][c] = 1
       
       for x in range(len(graph)):
           for y in range(len(graph[x])):
               if graph[x][y] == 1:
                   dfs(x, y)
                   count +=1
       print(count)

        







