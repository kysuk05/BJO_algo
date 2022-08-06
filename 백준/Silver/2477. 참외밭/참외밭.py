import sys

n = int(sys.stdin.readline())

arr = [[]for i in range(2)]

cnt = 0
for i in range(3):
    a,b = map(int,sys.stdin.readline().split())
    arr[0].append(b)
    a,b = map(int,sys.stdin.readline().split())
    arr[1].append(b)

ix = arr[0].index(max(arr[0]))
iy = arr[1].index(max(arr[1]))


mx = abs(arr[1][(ix-1)%3]-arr[1][(ix)%3])
my = abs(arr[0][iy]-arr[0][(iy+1)%3])

x = max(arr[0])
y = max(arr[1])

print(x*y*n-mx*my*n)