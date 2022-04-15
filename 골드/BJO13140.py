# N이 주어질 때 hello + world = N을 만족하는 
# 서로 다른 한 자리 자연수(0 포함) d, e, h, l, o, r, w를 구해서 
# 아래 그림과 같은 형태로 출력하는 프로그램을 작성하여라. 단, h와 w는 0이 될 수 없다.

from itertools import permutations

n = input()
ans = 0
for i in range(2):
    num_list = [0,1,2,3,4,5,6,7,8,9]
    if i == 0:
        l = int(n[-2]) // 2
        if int(n[-3]) >= l:
            r = int(n[-3])-l
        else:
            r = int(n[-3])+10-l
    
    elif i == 1:
        l = (int(n[-2])+10) // 2
        if (int(n[-3]))-1 >= l:
            r = int(n[-3])-1-l
        else:
            r = int(n[-3])+9-l
    
    if r == l:
        continue
    else:
        num_list.remove(r)
        num_list.remove(l)
    
    li = list(permutations(num_list, 5))
    for h,e,o,w,d in li:
        if h != 0 and w != 0 and h*10000 + w*10000 + e*1000+ o*1001 + l*120 + r*100 + d == int(n):
            ans = 1
            break
    if ans == 1:
        break

if ans == 1:
    print('  '+str(h)+str(e)+str(l)+str(l)+str(o))
    print('+ '+str(w)+str(o)+str(r)+str(l)+str(d))
    print('-------')
    if len(n) == 5:
        print('  '+n)
    else:
        print(' '+n)

else:
    print('No Answer')