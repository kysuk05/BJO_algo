# 각각 부피가 A, B, C(1≤A, B, C≤200) 리터인 세 개의 물통이 있다. 처음에는 앞의 두 물통은 비어 있고, 세 번째 물통은 가득(C 리터) 차 있다. 이제 어떤 물통에 들어있는 물을 다른 물통으로 쏟아 부을 수 있는데, 이때에는 한 물통이 비거나, 다른 한 물통이 가득 찰 때까지 물을 부을 수 있다. 이 과정에서 손실되는 물은 없다고 가정한다.

# 이와 같은 과정을 거치다보면 세 번째 물통(용량이 C인)에 담겨있는 물의 양이 변할 수도 있다. 첫 번째 물통(용량이 A인)이 비어 있을 때, 세 번째 물통(용량이 C인)에 담겨있을 수 있는 물의 양을 모두 구해내는 프로그램을 작성하시오.

from collections import deque

x,y,z = map(int,input().split())


x1 = 0
y1 = 0
z1 = z

qu = deque()
dic = {}

dic[(x1,y1,z1)] = 0
qu.append((0,0,z1))

while qu:
    dx,dy,dz = qu.pop()
    for i in range(6):
        if i == 0:
            tx = x-dx               #x에 남은 용량
            if tx <= dz:
                tz = dz-tx
                tx = x
            else:
                tx = dx+dz
                tz = 0
            if (tx,dy,tz) not in dic:
                dic[(tx,dy,tz)] = 0
                qu.append((tx,dy,tz))
        
        elif i == 1:
            ty = y-dy               #y에 남은 용량
            if ty <= dz:
                tz = dz-ty
                ty = y
            else:
                ty = dy+dz
                tz = 0
            if (dx,ty,tz) not in dic:
                dic[(dx,ty,tz)] = 0
                qu.append((dx,ty,tz))
        
        elif i == 2:
            tx = x-dx               
            if tx <= dy:
                ty = dy-tx
                tx = x
            else:
                tx = dx+dy
                ty = 0
            if (tx,ty,dz) not in dic:
                dic[(tx,ty,dz)] = 0
                qu.append((tx,ty,dz))
        
        elif i == 3:
            ty = y-dy       
            if ty <= dx:
                tx = dx-ty
                ty = y
            else:
                ty = dy+dx
                tx = 0
            if (tx,ty,dz) not in dic:
                dic[(tx,ty,dz)] = 0
                qu.append((tx,ty,dz))
        
        elif i == 4:
            tz = z-dz       
            if tz <= dx:
                tx = dx-tz
                tz = z
            else:
                tz = dz+dx
                tx = 0
            if (tx,dy,tz) not in dic:
                dic[(tx,dy,tz)] = 0
                qu.append((tx,dy,tz))
            
        elif i == 5:
            tz = z-dz       
            if tz <= dy:
                ty = dy-tz
                tz = z
            else:
                tz = dz+dy
                ty = 0
            if (dx,ty,tz) not in dic:
                dic[(dx,ty,tz)] = 0
                qu.append((dx,ty,tz))


ans = []           
for a,b,c in dic.keys():
    if a == 0:
        ans.append(c)
ans.sort()

for i in ans:
    print(i,end=' ')