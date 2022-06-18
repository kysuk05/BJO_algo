# 수강신청의 마스터 김종혜 선생님에게 새로운 과제가 주어졌다. 

# 김종혜 선생님한테는 Si에 시작해서 Ti에 끝나는 N개의 수업이 주어지는데, 최소의 강의실을 사용해서 모든 수업을 가능하게 해야 한다. 

# 참고로, 수업이 끝난 직후에 다음 수업을 시작할 수 있다. (즉, Ti ≤ Sj 일 경우 i 수업과 j 수업은 같이 들을 수 있다.)

# 수강신청 대충한 게 찔리면, 선생님을 도와드리자!

import sys
import heapq

n = int(sys.stdin.readline())

lesson = []
for i in range(n):
    a,b = map(int,sys.stdin.readline().split())
    lesson.append((a,b))

lesson.sort(reverse=1)

qu = [lesson[-1][1]]
lesson.pop()
ans = 1


while lesson:
    x,y = lesson.pop()
    t = heapq.heappop(qu)
    if t <= x:
        heapq.heappush(qu,y)
    else:
        heapq.heappush(qu,t)
        heapq.heappush(qu,y)


print(len(qu))