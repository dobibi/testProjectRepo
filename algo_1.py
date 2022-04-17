# -*- coding: utf-8 -*-

# [문제 1] : 거스름 돈 

from array import array

n = 1260
count = 0

# 큰 단위의 화폐부터 차례대로 확인

array = [500, 100, 50, 10]

for coin in array:
    #print("--coin 0--", coin)
    #print("----n 0----------",n)
    # 해당 화폐로 거슬러 줄 수 있는 동전의 개수 세기
    count += n//coin    
    #print("-----count-----",count)
    #print("----n 1----------",n)
    #print("--coin 1--", coin)
    n %= coin
    #print("------n 2--------",n)
print(count)

#분석
# 화폐의 종류가 K라고 할 때, 소스코드의 시간복잡도는 O(K)
# 이 알고리즘의 시간 복잡도는 거슬러줘야 하는 금액과는 무관하며, 동전의 총 종류에만 영향을 받음

