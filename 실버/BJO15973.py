# 2차원 좌표 평면 위에 두 개의 박스(직사각형) P, Q가 놓여 있다. 각 박스의 변은 x축이나 y축에 평행하다. 박스를 연구하는 학수는 이 두 박스의 교차 상태를 파악하여 내부가 겹쳐 있는지 (FACE), 그렇지 않고 선분에서 만나는 지(LINE), 그렇지 않고 한 점에서 만나는지(POINT), 아예 만나지 않는지 (NULL) 구별하려고 한다.

# 다음 그림은 두 박스의 여러 가지 교차 상태의 예를 보여준다.

				
# (a) POINT	(b) LINE	(c) FACE	(d) FACE	(e) NULL
# FACE인 경우에는 (d)처럼 어느 한 박스가 다른 박스에 포함될 수도 있다는 점에 유의해야 한다.

# 두 박스의 정보가 주어졌을 때, 두 박스의 교차 상태를 출력하는 프로그램을 작성하시오.


ax,ay,bx,by = map(int,input().split())

cx,cy,dx,dy = map(int,input().split())

ans = 'FACE'


    

if (ax == dx and (ay > cy and ay < dy)) or (ax == dx and (by > cy and by < dy)):
    ans = 'LINE'
elif (dx == ax and (cy > ay and cy < by)) or (dx == ax and (dy > ay and dy < by)):
    ans = 'LINE'
    
elif (ay == dy and (ax > cx and ax < dx)) or (ay == dy and (bx > cx and bx < dx)):
    ans = 'LINE'
elif (dy == ay and (cx > ax and cx < bx)) or (dy == ay and (dx > ax and dx < bx)):
    ans = 'LINE'

elif (bx == cx and (ay > cy and ay < dy)) or (bx == cx and (by > cy and by < dy)):
    ans = 'LINE'
elif (cx == bx and (cy > ay and cy < by)) or (cx == bx and (dy > ay and dy < by)):
    ans = 'LINE'

elif (by == cy and (ax > cx and ax < dx)) or (by == cy and (bx > cx and bx < dx)):
    ans = 'LINE'
elif (cy == by and (cx > ax and cx < bx)) or (cy == by and (dx > ax and dx < bx)):
    ans = 'LINE'
elif ((bx,by)==(cx,dy) and by>cy) or ((bx,ay)==(cx,cy) and dy>ay) or ((dx,cy)==(ax,ay) and by>cy) or ((dx,dy)==(ax,by) and dy>ay) or ((bx,by)==(cx,dy) and (bx,ay)==(cx,cy)) or ((ax,ay)==(dx,cy) and (dx,dy)==(ax,by)) or ((cx, cy) == (ax, by) and (bx, by) == (dx, cy)) or ((ax, ay) == (cx, dy) and (dx, dy) == (bx, ay)):
    ans = 'LINE'


if ax == dx and by == cy:
    ans = 'POINT'
elif bx == cx and by == cy:
    ans = 'POINT'
elif ax == dx and ay == dy:
    ans = 'POINT'
elif bx == cx and ay == dy:
    ans = 'POINT'


if bx < cx or dx < ax or by < cy or dy < ay:
    ans = 'NULL'
elif bx-ax < dx-cx and by-ay < dy-cy and (cx<ax<dx and cx<bx<dx) and (cy<ay<dy and cy<by<dy):
    ans = 'NULL'
elif bx-ax > dx-cx and by-ay > dy-cy and (ax<cx<bx and ax<dx<bx) and (ay<cy<by and ay<dy<by):
    ans = 'NULL'



print(ans)
