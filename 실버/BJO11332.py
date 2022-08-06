# 유빈이는 코딩을 하다가 시간 초과가 났다. 그래서 시간 복잡도를 계산하기로 했다.

# 채점 시스템은 1초에 100000000(108)가지 동작을 할 수 있다.

# 여러분들은 유빈이를 도와 시간초과가 나는지 확인하는 프로그램을 작성하라.


import sys

t = int(sys.stdin.readline())

for i in range(t):
    ans = 'May Pass.'
    S,N,T,L = sys.stdin.readline().split()
    if '^2' in S:
        temp = int(N)**2*int(T)
        if temp > 100000000*int(L):
            ans = 'TLE!'
    elif '^3' in S:
        temp = int(N)**3*int(T)
        if temp > 100000000*int(L):
            ans = 'TLE!'
    elif '2^' in S:
        temp = 2**int(N)*int(T)
        if temp > 100000000*int(L):
            ans = 'TLE!'
    elif 'N!' in S:
        if int(N) > 15:
            ans = 'TLE!'
        else:
            temp = 1
            N = int(N)
            while N > 1:
                temp *= N
                N -= 1
            temp *= int(T)
            if temp > 100000000*int(L):
                ans = 'TLE!'
    else:
        temp = int(N)*int(T)
        if temp > 100000000*int(L):
                ans = 'TLE!'
    print(ans)