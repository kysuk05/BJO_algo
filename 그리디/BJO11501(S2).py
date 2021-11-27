# 홍준이는 요즘 주식에 빠져있다. 그는 미래를 내다보는 눈이 뛰어나, 날 별로 주가를 예상하고 언제나 그게 맞아떨어진다. 매일 그는 아래 세 가지 중 한 행동을 한다.

# 주식 하나를 산다.
# 원하는 만큼 가지고 있는 주식을 판다.
# 아무것도 안한다.
# 홍준이는 미래를 예상하는 뛰어난 안목을 가졌지만, 어떻게 해야 자신이 최대 이익을 얻을 수 있는지 모른다. 따라서 당신에게 날 별로 주식의 가격을 알려주었을 때, 최대 이익이 얼마나 되는지 계산을 해달라고 부탁했다.

# 예를 들어 날 수가 3일이고 날 별로 주가가 10, 7, 6일 때, 주가가 계속 감소하므로 최대 이익은 0이 된다. 그러나 만약 날 별로 주가가 3, 5, 9일 때는 처음 두 날에 주식을 하나씩 사고, 마지막날 다 팔아 버리면 이익이 10이 된다.


#스택을 이용한 풀이(그리디 아님)

import sys

t = int(sys.stdin.readline())

for i in range(t):
    n = int(sys.stdin.readline())
    li = list(map(int,sys.stdin.readline().split()))
    stack = []
    for j in range(n):
        l1 = li[j]
        l2 = 1
        l3 = 0
        if stack and stack[-1][0]<li[j]:
            while stack:
                if stack[-1][0]<li[j]:
                    s1,s2,s3 = stack.pop()
                    l2 = l2 + s2
                    l3 = l3 + s3 + (li[j]-s1)*s2
                else:
                    break
            stack.append((l1,l2,l3))
        else:
            stack.append((l1,l2,l3))
    
    ans = sum(list(map(lambda x: x[2],stack)))
    print(ans)


#그리디

import sys
t=int(sys.stdin.readline())
for k in range(t):
    n=int(sys.stdin.readline())
    data=list(map(int,sys.stdin.readline().split()))
    mn = 0
    ans = 0
    for i in range(len(data)-1,-1,-1):
        if mn>data[i]:
            ans+=(mn-data[i])
        else:
            mn = data[i]
    print(ans)