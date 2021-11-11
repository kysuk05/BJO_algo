# 자연수 N과 M이 주어졌을 때, 
# 아래 조건을 만족하는 길이가 M인 수열을 모두 구하는 프로그램을 작성하시오.

# 1부터 N까지 자연수 중에서 M개를 고른 수열
# 같은 수를 여러 번 골라도 된다.
# 고른 수열은 비내림차순이어야 한다.
# 길이가 K인 수열 A가 A1 ≤ A2 ≤ ... ≤ AK-1 ≤ AK를 만족하면, 비내림차순이라고 한다.


n,m = map(int,input().split())

lis = [0]*10

def func(k):
    if k == m:
        for i in range(m):
            print(lis[i],end=' ')
        print()
        return
    for j in range(1,n+1):
        if lis[k-1] <= j:
            lis[k] = j
            func(k+1)
        
func(0)