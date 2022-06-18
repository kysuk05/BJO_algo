# 2×n 직사각형을 2×1과 2×2 타일로 채우는 방법의 수를 구하는 프로그램을 작성하시오.

# 아래 그림은 2×17 직사각형을 채운 한가지 예이다.


import sys
tile = [1,1,3,5]



for i in range(124):
    tile.append(tile[-2]*2+tile[-1])
    tile.append((tile[-1]*2)-1)


while True:
    try:
        test = int(sys.stdin.readline())
        print(tile[test])
    except:
        break