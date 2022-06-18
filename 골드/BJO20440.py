# 🎵니가 싫어 싫어 너무 싫어 싫어 오지마 내게 찝쩍대지마🎵 - 유자, 모기송 中

# 모기를 싫어하는 지동이는 어느 날 문득 자신의 방에 모기가 가장 많이 있는 시간대가 언제인지 궁금해졌다. 다행히 지동이 방은 최첨단 시스템이 갖춰져 있어 어떤 모기가 방에 언제 입장했고 언제 퇴장했는지를 기록할 수 있다.

# 지동이를 도와 모기들의 방 입장, 퇴장 시각이 주어졌을 때 모기들이 가장 많이 있는 시간대와 해당 시간대에 모기가 몇 마리가 있는지 구하는 프로그램을 만들어보자. 


import sys
import heapq as hq

n = int(sys.stdin.readline())
mosq = []

for i in range(n):
    e,x = map(int,sys.stdin.readline().split())
    mosq.append((e,x))

mosq.sort()


heap = []
ans = 0
mos_range = [0,0]

for i in range(n):
    while heap and heap[0][0] <= mosq[i][0]:
        hq.heappop(heap)
    hq.heappush(heap,(mosq[i][1],mosq[i][0]))
    
    if len(heap) == ans and mos_range[1] == mosq[i][0]:
        mos_range[1] = heap[0][0]
    elif len(heap) > ans:
        ans = len(heap)
        mos_range = [mosq[i][0],heap[0][0]]

print(ans)
print(*mos_range)