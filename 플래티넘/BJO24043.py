import sys

sys.setrecursionlimit(10**6)

n = int(sys.stdin.readline())
li = list(map(int,sys.stdin.readline().split()))
di = {}
che = []
for i in range(len(li)):
    check = 0
    if li[i] in che:
        continue
    di[len(di)+1] = i+1
    for j in range(len(che)):
        che.append(li[i]^che[j])
    che.append(li[i])
    
print(2**len(di)-1)
def back(n):
    if n == 1:
        print(di[n])
    else:
        back(n-1)
        print(di[n])
        back(n-1)
back(len(di))