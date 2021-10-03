# 총 10개의 줄에 걸쳐 한 줄에 하나씩 10개의 구간이 주어진다. i번째 줄에는 i번째 구간의 시작 위치 ai와 끝 위치 bi가 차례대로 주어진다. 이때 두 값의 범위는 1 ≤ ai ≤ bi ≤ 20이다.

# 1부터 20까지 오름차순으로 놓인 카드들에 대해, 입력으로 주어진 10개의 구간 순서대로 뒤집는 작업을 했을 때 마지막 카드들의 배치를 한 줄에 출력한다. 

a = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
k = 0
for i in range(10):
    num1,num2=map(int,input().split())
    b = a[num1-1:num2]
    b.reverse()
    for i in range(len(b)):
        a.remove(b[i])
    
    for j in range(num1-1,num2):
        a.insert(j,b[k])
        k+=1
    k = 0
for i in range(len(a)):
    print(a[i],end=' ')