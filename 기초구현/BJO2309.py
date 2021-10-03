#아홉 개의 줄에 걸쳐 난쟁이들의 키가 주어진다. 
# 주어지는 키는 100을 넘지 않는 자연수이며, 아홉 난쟁이의 키는 모두 다르며, 
# 가능한 정답이 여러 가지인 경우에는 아무거나 출력한다.
# 일곱 난쟁이의 키를 오름차순으로 출력한다. 
# 일곱 난쟁이를 찾을 수 없는 경우는 없다.
a = []
for i in range(9):
    a.append(int(input()))
k = True

b = sum(a)
while k:
    for i in range(len(a)):
        for j in range(i+1,len(a)):
            if b-(a[i]+a[j]) == 100:
                n1 = a[i]
                n2 = a[j]
                a.remove(n1)
                a.remove(n2)
                k = False
                break
a.sort()
for i in range(len(a)):
    print(a[i])