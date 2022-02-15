T = int(input())

for i in range(1,T+1):
    n1,n2 = map(int,input().split())
    a = min(n1,n2)
    b = max(n1,n2)
    
    lay_a = int((a*2)**0.5)
    lay_b = int((b*2)**0.5)
    
    if a>(lay_a+1)*lay_a//2:
        lay_a += 1
    if b>(lay_b+1)*lay_b//2:
        lay_b += 1
    
    a = (lay_a,a-(lay_a-1)*lay_a//2)
    b = (lay_b,b-(lay_b-1)*lay_b//2)
    
    if a[0]-b[0] < a[1]-b[1]:
        if b[1] > a[1]:
            print('#'+str(i),abs(a[1]-b[1]))
        else:
            print('#'+str(i),abs(a[1]-b[1])+abs(a[0]-b[0]))
    else:
        if b[1] > a[1]:
            print('#'+str(i),abs(a[0]-b[0]))
        else:
            print('#'+str(i),abs(a[1]-b[1])+abs(a[0]-b[0]))