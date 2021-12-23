# 트판은 평평한 판과 동심원이 그려진 원형 코르크로 만든다. 사람들은 다트를 다트판에서 가장 중심에 있는 원(불스아이)을 향해 던진다.

# 다트판의 각 고리에는 점수가 적혀있고, 중심에 가까울수록 점수가 높다.



# 각 고리의 반지름은 3cm, 6cm, 9cm, 12cm, 15cm이다. (따라서, 불스아이의 지름은 6cm) 간단한 다트게임은 두 플레이어가 게임을 하며, 다음과 같이 플레이한다.

# 첫 번째 플레이어가 다트 3개를 다트판에 던진다. 다트가 맞춘 영역의 점수의 합이 그 플레이어의 점수가 된다. 첫 번째 플레이어가 던진 다트를 다트판에서 모두 제거한다. 두 번째 플레이어가 다트 3개를 다트판에 던진 뒤, 점수를 계산한다. 높은 점수를 얻은 플레이어가 이긴다.

# 두 플레이어의 점수를 계산한 뒤, 누가 이기는지를 구하는 프로그램을 작성하시오. 만약 다트가 경계에 걸쳐있다면, 높은 점수를 얻은 것이다. 다트가 다트판 밖을 맞춘다면, 점수를 얻지 못한다. Double precision floating point 연산을 사용하면 된다.

import sys
n = int(sys.stdin.readline())
for i in range(n):
    li = list(map(float,sys.stdin.readline().split()))
    su1 = 0
    su2 = 0
    for i in range(0,5,2):
        sc = li[i]**2+li[i+1]**2
        if sc <= 9:
            su1 += 100
        elif sc <= 36:
            su1 += 80
        elif sc <= 81:
            su1 += 60
        elif sc <= 144:
            su1 += 40
        elif sc <= 225:
            su1 += 20
    for i in range(6,11,2):
        sc = li[i]**2+li[i+1]**2
        if sc <= 9:
            su2 += 100
        elif sc <= 36:
            su2 += 80
        elif sc <= 81:
            su2 += 60
        elif sc <= 144:
            su2 += 40
        elif sc <= 225:
            su2 += 20
    if su1 == su2:
        print('SCORE: '+str(su1)+' to '+str(su2)+', TIE.')
    elif su1 > su2:
        print('SCORE: '+str(su1)+' to '+str(su2)+', PLAYER 1 WINS.')
    else:
        print('SCORE: '+str(su1)+' to '+str(su2)+', PLAYER 2 WINS.')