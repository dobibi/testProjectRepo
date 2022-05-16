#dfs로 풀기

n = int(input())
graph = [[0]*n for _ in range(n)]
visited = [[False]*n for _ in range(n)]

#입력값을 graph에 기입

for i in range(n):
    line = input()
    for j, b in enumerate(line):
        graph[i][j] = int(b)
        
# 상하좌우 이동 설정

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]


def dfs(x, y):
    global cnt   #cnt를 사용하기 위해 global 선언
    visited[x][y] = True
    if graph[x][y] == 1:
        cnt +=1
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        
        if 0 <= nx < n and  0 <= ny < n:
            if visited[nx][ny] == False and graph[nx][ny] == 1:
                dfs(nx, ny)     

cnt = 0
housing =[]

#정의된 dfs를 가지고 graph를 탐색

for i in range(n):
    for j in range(n):
        if graph[i][j] == 1 and visited[i][j] == False:
            dfs(i, j)
            housing.append(cnt)
            cnt = 0
            
#문제 답 도출
housing.sort()  #오름차순 정렬
print(len(housing))
for i in housing:
    print(i)            

                