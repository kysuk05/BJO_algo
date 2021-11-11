# 자연수 N과 M이 주어졌을 때, 아래 조건을 만족하는 길이가 M인 수열을 모두 구하는 프로그램을 작성하시오.

# 1부터 N까지 자연수 중에서 M개를 고른 수열
# 같은 수를 여러 번 골라도 된다.


n,m = map(int,input().split())

lis = []

def func(k):
    if k == m:
        for i in range(m):
            print(lis[i],end=' ')
        print()
        return
    else:
        for j in range(1,n+1):
            lis.append(j)
            func(k+1)
            lis.pop()

func(0)


# 비슷한 방법


n,m = map(int,input().split())

lis = [0]*10

def func(k):
    if k == m:
        for i in range(m):
            print(lis[i],end=' ')
        print()
        return
    else:
        for j in range(1,n+1):
            lis[k] = j
            func(k+1)

func(0)