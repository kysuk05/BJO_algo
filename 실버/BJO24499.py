# 오늘도 블롭은 배고프다. 그래서 블롭은 요리사 연우를 찾아가 맛있는 것을 달라고 부탁했다.

# 연우는 귀여운 블롭에게 이왕이면 맛있는 음식을 해 주고 싶었기에, 자신이 만드는 데에 가장 뛰어난 애플파이를 만들기로 하였다. 
# 연우는 $N$개의 애플파이를 만들었으며, 이를 원 모양으로 책상에 배치해 놓았다.

# 각 애플파이는 하나의 양의 정수로 표현되며, 이는 맛있는 정도를 의미한다. (수가 클수록 더 맛있는 애플파이이다.)



# 블롭은 $N$개의 애플파이 중 $K$개를 먹으려고 한다. 물론 블롭은 힘을 들이지 않고 먹고 싶기 때문에, 연속으로 배치되어 있는 $K$개의 애플파이를 먹으려 한다.

# 블롭을 도와서 블롭이 먹을 애플파이의 맛의 합의 최댓값을 구해 주자!


import sys

N,K = map(int,sys.stdin.readline().split())

li = list(map(int,sys.stdin.readline().split()))

t = li[:K-1]
for i in t:
    li.append(i)


st = 0
en = 0

ans = 0
total = 0

while True:
    total += li[en]
    en += 1
    if en-st > K:
        total -= li[st]
        st += 1
    
    if total > ans:
        ans = total
    if en == len(li):
        break

print(ans)
    