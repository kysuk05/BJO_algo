# 표준 입력으로 다음 정보가 주어진다. 첫 번째 줄에는 수학여행에 참가하는 학생 수를 나타내는 정수 N(1 ≤ N ≤ 1,000)과 한 방에 배정할 수 있는 최대 인원 수 K(1 < K ≤ 1,000)가 공백으로 분리되어 주어진다. 다음 N 개의 각 줄에는 학생의 성별 S와 학년 Y(1 ≤ Y ≤ 6)가 공백으로 분리되어 주어진다. 성별 S는 0, 1중 하나로서 여학생인 경우에 0, 남학생인 경우에 1로 나타낸다. 

# 출력
# 표준 출력으로 학생들을 모두 배정하기 위해 필요한 최소한의 방의 수를 출력한다.
import sys
a,b = map(int,sys.stdin.readline().split())
std_gir = [0]*6
std_boy = [0]*6
for i in range(a):
    c,d = map(int,sys.stdin.readline().split())
    if c == 0 :
        std_gir[d-1] += 1
    else :
        std_boy[d-1] += 1
ans = 0
for i in range(6):
    ans+=(std_gir[i]+b-1)//b
    ans+=(std_boy[i]+b-1)//b
print(ans)