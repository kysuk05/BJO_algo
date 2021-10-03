#다섯 개의 자연수가 주어질 때 이들의 평균과 중앙값을 구하는 프로그램을 작성하시오.
a = []
for i in range(5):
    a.append(int(input()))
a.sort()

print(int(sum(a)/5))
print(a[2])