# 첫째 줄에 두 수 사이에 있는 수의 개수를 출력한다.

# 둘째 줄에는 두 수 사이에 있는 수를 오름차순으로 출력한다.

a,b=map(int,input().split())
if b > a:
    ans1 = b-a-1
elif a > b:
    ans1 = a-b-1
else:
    ans1 = 0
print(ans1)
if ans1 != 0:
    for i in range(1,ans1+1):
        print(min(a,b)+i,end=' ')