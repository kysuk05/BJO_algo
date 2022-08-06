# 크기가 H×W인 모눈종이와 스티커 N개가 있다. i번째 스티커의 크기는 Ri×Ci이다. 모눈종이는 크기가 1×1인 칸으로 나누어져 있으며, 간격 1을 두고 선이 그어져 있다.

# 오늘은 모눈종이에 스티커 2개를 붙이려고 한다. 스티커의 변은 격자의 선과 일치하게 붙여야 하고, 두 스티커가 서로 겹치면 안 된다. 단, 스티커가 접하는 것은 가능하다. 스티커를 90도 회전시키는 것은 가능하다. 스티커가 모눈종이를 벗어나는 것은 불가능하다.

# 두 스티커가 붙여진 넓이의 최댓값을 구해보자.

import sys

H,W = map(int,sys.stdin.readline().split())

n = int(sys.stdin.readline())

sticker = []

for i in range(n):
    a,b = sorted(map(int,sys.stdin.readline().split()))
    sticker.append([a,b])

check = []

for i in range(len(sticker)):
    for j in range(i):
        if (sticker[i][1] + sticker[j][0] <= H and max(sticker[i][0], sticker[j][1]) <= W) or (max(sticker[i][1], sticker[j][0]) <= W and sticker[i][0] + sticker[j][1] <= H) or (sticker[i][1] + sticker[j][0] <= W and max(sticker[i][0], sticker[j][1]) <= H) or (max(sticker[i][1], sticker[j][0]) <= H and sticker[i][0] + sticker[j][1] <= W) or (
            sticker[i][1] + sticker[j][1] <= H and max(sticker[i][0], sticker[j][0]) <= W) or (max(sticker[i][1], sticker[j][1]) <= H and sticker[i][0] + sticker[j][0] <= W) or (max(sticker[i][1] , sticker[j][1]) <= W and sticker[i][0] + sticker[j][0] <= H) or (sticker[i][1] + sticker[j][1] <= W and max(sticker[i][0], sticker[j][0]) <= H):
            check.append(sticker[i][0]*sticker[i][1] + sticker[j][0]*sticker[j][1])

if not check:
    print(0)
else:
    print(max(check))