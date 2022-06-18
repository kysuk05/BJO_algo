# 두 정수 A와 B가 있을 때, A에 포함된 숫자의 순서를 섞어서 새로운 수 C를 만들려고 한다. 즉, C는 A의 순열 중 하나가 되어야 한다. 

# 가능한 C 중에서 B보다 작으면서, 가장 큰 값을 구해보자. C는 0으로 시작하면 안 된다.

from itertools import permutations

a,b = input().split()

if len(a) > len(b):
    print(-1)
else:
    a = list(a)
    a.sort()
    a_list = list(permutations(a,len(a)))
    if len(a) < len(b):
        print(''.join(a_list[-1]))
    else:
        ind = 0
        for i in range(len(a_list)):
            temp = ''.join(a_list[i])
            if temp[0] == '0':
                continue
            if int(temp) >= int(b):
                break
            ind = i
        
        if ind == 0:
            print(-1)
        else:
            print(''.join(a_list[ind]))