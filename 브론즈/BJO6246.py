# 매년 가을 대전에서 열리는 대학생 프로그래밍 대회의 묘미 중 하나는 풍선 놀이이다. 시상식에서 스코어보드 공개를 기다리다가 심심해지면, 주위에 있는 풍선을 엮어서, 대회장을 가로지르는 긴 풍선 줄을 만드는 것이다! 이 풍선을 아치형으로 단상 위에 올리면, 본인의 잉여로움을 참가자들에게 뽐낼 수 있는 기회가 생긴다.

# 심심해진 재현이와 한필이는 풍선 놀이를 위해서 기다란 풍선 줄을 가져왔다. 풍선 줄에는 풍선을 매달 수 있는 N개의 슬롯이 있으며, 각 슬롯은 1번부터 N번까지 번호가 붙어있다. 풍선 줄에, 한필이는 Q번에 걸쳐서 규칙적으로 풍선을 꽂았다. 예를 들면, ’1번 슬롯부터 3개씩 띄어서 풍선을 놓자’ 라고 한필이가 생각했다면, 1, 4, 7, 10, ... 번째 슬롯에 풍선을 놓으며, 슬롯의 번호가 N을 초과하면 풍선을 놓는 것을 그만둔다. 이미 풍선이 놓여진 슬롯은 건너 뛴다.

# Q번에 걸친 풍선 설치가 끝난 후, 한필이는 어떤 슬롯들이 비어 있는 것을 확인했다. 이 슬롯을 메꾸는 풍선을 가져오기 위해서, 총 몇 개의 슬롯이 비었는지를 계산해주자.



import sys

n,m = map(int,sys.stdin.readline().split())

li = [1]*(n+1)
li[0] = 0

for i in range(m):
    x,y = map(int,sys.stdin.readline().split())
    li[x] = 0
    while x+y <= n:
        x+=y
        li[x] = 0
print(sum(li))