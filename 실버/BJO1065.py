# 어떤 양의 정수 X의 각 자리가 등차수열을 이룬다면, 그 수를 한수라고 한다. 등차수열은 연속된 두 개의 수의 차이가 일정한 수열을 말한다. 
# N이 주어졌을 때, 1보다 크거나 같고, N보다 작거나 같은 한수의 개수를 출력하는 프로그램을 작성하시오. 


n = int(input())

li = []
for i in range(1,n+1):
    k = str(i)
    if (len(k) == 1) or (len(k) == 2):
        li.append(k)
    else:
        if int(k[1])-int(k[0]) == int(k[2])-int(k[1]):
            li.append(k)
            
print(len(li))