# 철수와 민수는 카드 게임을 즐겨한다. 이 카드 게임의 규칙은 다음과 같다.

# N개의 빨간색 카드가 있다. 각각의 카드는 순서대로 1부터 N까지 번호가 매겨져 있다. 이 중에서 M개의 카드를 고른다.
# N개의 파란색 카드가 있다. 각각의 카드는 순서대로 1부터 N까지 번호가 매겨져 있다. 이 중에서 빨간색에서 고른 번호와 같은 파란색 카드 M개를 고른다.
# 철수는 빨간색 카드를 가지고 민수는 파란색 카드를 가진다.
# 철수와 민수는 고른 카드 중에 1장을 뒤집어진 상태로 낸다. 그리고 카드를 다시 뒤집어서 번호가 큰 사람이 이긴다. 이 동작을 K번 해서 더 많이 이긴 사람이 최종적으로 승리한다. 한 번 낸 카드는 반드시 버려야 한다.
# 철수는 뛰어난 마술사이기 때문에 본인이 낼 카드를 마음대로 조작할 수 있다. 즉, 카드를 버리고 민수 몰래 다시 들고 온다거나 민수한테 없는 카드를 내기도 한다.

# 민수는 뛰어난 심리학자이기 때문에 철수가 낼 카드를 알아낼 수 있다. 그래서 민수는 철수가 낼 카드보다 큰 카드가 있다면 그 카드들 중 가장 작은 카드를 내기로 했다.

# K번 동안 철수가 낼 카드가 입력으로 주어진다. 그렇다면 민수가 어떤 카드를 낼지 출력하라. 단, 민수가 카드를 내지 못하는 경우는 없다고 가정한다.

import sys
import bisect

N,M,K = map(int,sys.stdin.readline().split())

card = sorted(list(map(int,sys.stdin.readline().split())))

dic_card = {}
for i in card:
    dic_card[i] = 0
ch = list(map(int,sys.stdin.readline().split()))

for i in ch:
    k = bisect.bisect_right(card,i)
    if dic_card[card[k]] == 0:
        print(card[k])
        dic_card[card[k]] = 1
    else:
        while True:
            k += 1
            if dic_card[card[k]] == 0:
                print(card[k])
                dic_card[card[k]] = 1
                break