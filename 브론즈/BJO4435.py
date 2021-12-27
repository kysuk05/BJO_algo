# 중간계에 전쟁이 일어나려고 한다. 간달프는 사우론에 대항하기 위한 군대를 소집했고, 여러 종족이 이 군대에 가담했다. 전쟁을 시작하기 전에 간달프는 각 종족에 점수를 매겼다.

# 간달프의 군대의 각 종족의 점수는 다음과 같다.

# 호빗 - 1
# 인간 - 2
# 엘프 - 3
# 드워프 - 3
# 독수리 - 4
# 마법사 - 10
# 사우론의 군대의 점수는 다음과 같다.

# 오크 - 1
# 인간 - 2
# 워그(늑대) - 2
# 고블린 - 2
# 우럭하이 - 3
# 트롤 - 5
# 마법사 - 10
# 중간계는 매우 신비한 곳이어서 각 전투의 승리는 날씨, 장소, 용맹에 영향을 받지 않는다. 전투에 참여한 각 종족의 점수를 합한 뒤, 큰 쪽이 이긴다.

# 전투에 참여한 종족의 수가 주어졌을 때, 어느 쪽이 이기는지 구하는 프로그램을 작성하시오.



import sys
n = int(sys.stdin.readline())


for i in range(n):
    a = list(map(int,sys.stdin.readline().split()))
    b = list(map(int,sys.stdin.readline().split()))
    an1 = a[0]*1 + a[1]*2 + a[2]*3 + a[3]*3 + a[4]*4 + a[5]*10
    an2 = b[0]*1 + b[1]*2 + b[2]*2 + b[3]*2 + b[4]*3 + b[5]*5 + b[6]*10
    print('Battle '+str(i+1)+': ',end='')
    if an1 > an2:
        print("Good triumphs over Evil")
    elif an2 > an1:
        print("Evil eradicates all trace of Good")
    else:
        print("No victor on this battle field")