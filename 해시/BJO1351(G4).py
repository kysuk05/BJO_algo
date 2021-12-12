# 무한 수열 A는 다음과 같다.

# A0 = 1
# Ai = A⌊i/P⌋ + A⌊i/Q⌋ (i ≥ 1)
# N, P와 Q가 주어질 때, AN을 구하는 프로그램을 작성하시오.

n,p,q = map(int,input().split())

di = {}
di[0] = 1 


def infi(num):
    if num in di:
        return di[num]
    else:
        di[num] = infi(num//p) + infi(num//q)
        return di[num]
print(infi(n))