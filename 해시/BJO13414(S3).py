# 입력 데이터는 표준 입력을 사용한다. 입력은 1개의 테스트 데이터로 구성된다. 입력의 첫 번째 줄에는 과목의 수강 가능 인원 K(1 ≤ K ≤ 100,000)와 학생들이 버튼을 클릭한 순서를 기록한 대기목록의 길이 L(1 ≤ L ≤ 500,000)이 주어진다. 두 번째 줄부터 L개의 줄에는 수강신청을 버튼을 클릭한 학생의 학번이 클릭 순서대로 주어진다. 학번은 8자리의 숫자로 이루어져 있다.

# 출력
# 출력은 표준 출력을 사용한다. 입력받은 데이터에 대해, 수강신청 관리 시스템의 규칙을 적용한 후 수강신청에 성공한 인원의 학번을 한 줄에 1개씩 출력한다.

import sys

n,m = map(int,sys.stdin.readline().split())
di = {}
for i in range(m):
    k = sys.stdin.readline().rstrip()
    if k not in di:
        di[k] = 0
    else:
        di.pop(k)
        di[k] = 0
li = list(di.keys())
if n < len(li):
    for j in range(n):
        print(li[j])
else:
    for j in range(len(li)):
        print(li[j])
