# 수현이는 카드 기술을 연습하고 있다. 수현이의 손에 들린 카드를 하나씩 내려놓아 바닥에 쌓으려고 한다. 수현이가 쓸 수 있는 기술은 다음 3가지다.

# 제일 위의 카드 1장을 바닥에 내려놓는다.
# 위에서 두 번째 카드를 바닥에 내려놓는다. 카드가 2장 이상일 때만 쓸 수 있다.
# 제일 밑에 있는 카드를 바닥에 내려놓는다. 카드가 2장 이상일 때만 쓸 수 있다.
# 수현이는 처음에 카드 N장을 들고 있다. 카드에는 1부터 N까지의 정수가 중복되지 않게 적혀 있다. 기술을 N번 사용하여 카드를 다 내려놓았을 때, 놓여 있는 카드들을 확인했더니 위에서부터 순서대로 1, 2, …, N이 적혀 있었다!

# 놀란 수현이는 처음에 카드가 어떻게 배치되어 있었는지 궁금해졌다. 처음 카드의 상태를 출력하여라.


import sys
from collections import deque

n = int(sys.stdin.readline())

arr = list(map(int,sys.stdin.readline().split()))
arr.reverse()

num_list = list(range(1,n+1))

ans = deque()

for i in range(len(arr)):
    if arr[i] == 1:
        ans.append(num_list[i])
    elif arr[i] == 2:
        temp = ans.pop()
        ans.append(num_list[i])
        ans.append(temp)
    else:
        ans.appendleft(num_list[i])

ans.reverse()
print(*ans)