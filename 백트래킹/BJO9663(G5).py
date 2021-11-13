# 문제
# N-Queen 문제는 크기가 N × N인 체스판 위에 퀸 N개를 서로 공격할 수 없게 놓는 문제이다.

# N이 주어졌을 때, 퀸을 놓는 방법의 수를 구하는 프로그램을 작성하시오.

n = int(input())

#y값 확인
che1 = [0]*n*(n+2)
#왼쪽 대각선 확인
che2 = [0]*n*(n+2)
#오른쪽 대각선 확인
che3 = [0]*n*(n+2)

ans = 0

def Queen(k):
    global ans
    if k == n:
        ans+=1
        return
    for i in range(n):
        if che1[i] == 0 and che2[k+i] == 0 and che3[k-i+n] == 0:
            che1[i] = 1
            che2[k+i] = 1
            che3[k-i+n] = 1
            Queen(k+1)
            che1[i] = 0
            che2[k+i] = 0
            che3[k-i+n] = 0
Queen(0)
print(ans)