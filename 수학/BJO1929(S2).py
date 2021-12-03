# M이상 N이하의 소수를 모두 출력하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 자연수 M과 N이 빈 칸을 사이에 두고 주어진다. 
# (1 ≤ M ≤ N ≤ 1,000,000) M이상 N이하의 소수가 하나 이상 있는 입력만 주어진다.


n,m = map(int,input().split())
k = list(range(n,m+1))


for i in k:
    check = 0
    if i == 1:
        continue
    if i == 2:
        print(i)
    else:
        for j in range(2,int(i**(1/2))+1):
            if i % j == 0:
                check = 1
                break
        if check == 0:
            print(i)
        else:
            check = 0