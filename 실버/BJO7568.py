# 첫 줄에는 전체 사람의 수 N이 주어진다. 그리고 이어지는 N개의 줄에는 각 사람의 몸무게와 키를 나타내는 양의 정수 x와 y가 하나의 공백을 두고 각각 나타난다.

# 출력
# 여러분은 입력에 나열된 사람의 덩치 등수를 구해서 그 순서대로 첫 줄에 출력해야 한다. 단, 각 덩치 등수는 공백문자로 분리되어야 한다.

n = int(input())

li = []
for i in range(n):
    x,y = map(int,input().split())
    li.append((x,y))
ans = []
for j in li:
    rank = 1
    for k in li:
        if (j[0] < k[0]) and (j[1] < k[1]):
            rank += 1
    ans.append(rank)

for _ in ans:
    print(_,end=' ')