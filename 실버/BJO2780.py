# 석원이는 자신의 현관문에 비밀번호 기계를 설치했다. 그 기계의 모양은 다음과 같다.



# 지나가던 석원이 친구 주희는 단순한 호기심에 저 비밀번호를 풀고 싶어한다. 이때 주희는 바닥에 떨어져 있는 힌트 종이를 줍게 된다. 이 종이에는 석원이가 비밀번호를 만들 때 사용했던 조건이 적혀 있다. 이제 주희는 이 조건을 가지고, 석원이 집의 가능한 비밀번호의 전체 개수를 알고 싶어 한다. 현재 컴퓨터를 사용할 수 없는 주희는 당신에게 이 문제를 부탁했다. 석원이의 힌트 종이는 다음과 같다.

# 비밀번호의 길이는 N이다.
# 비밀번호는 위 그림에 나온 번호들을 눌러서 만든다.
# 비밀번호에서 인접한 수는 실제 위 기계의 번호에서도 인접해야 한다.
# (ex. 15 라는 비밀번호는 불가능하다. (1과 5는 인접하지 않는다. ) 하지만 1236이라는 비밀번호는 가능하다.)

import sys


n = int(sys.stdin.readline())
for i in range(n):
    password = [1,1,1,1,1,1,1,1,1,1]
    t = int(sys.stdin.readline())
    for j in range(t-1):
        temp = password[:]
        temp[0] = password[7]
        temp[1] = password[2]+password[4]
        temp[2] = password[1]+password[5]+password[3]
        temp[3] = password[2]+password[6]
        temp[4] = password[1]+password[5]+password[7]
        temp[5] = password[2]+password[6]+password[4]+password[8]
        temp[6] = password[3]+password[5]+password[9]
        temp[7] = password[4]+password[8]+password[0]
        temp[8] = password[5]+password[7]+password[9]
        temp[9] = password[8]+password[6]
        password = temp
    print(sum(password)%1234567)