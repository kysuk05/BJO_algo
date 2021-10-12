#N개의 수가 주어졌을 때, 이를 오름차순으로 정렬하는 프로그램을 작성하시오.
a = int(input())
b = []
for i in range(1,a+1):
    b.append(int(input()))

b.sort()
for i in range(len(b)):
    print(b[i])