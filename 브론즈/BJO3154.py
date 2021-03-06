# 우리가 핸드폰으로 알람시계를 설정할 때는 시간과 분을 나타내는 4개의 숫자를 입력하기 위해 키보드를 사용한다. 예를 들어, 우리가 12:30으로 알람을 설정하려고 한다면 1,2,3,0을 입력하면 되고 9시30분 같은 경우는 맨 앞에 0을 붙여 0,9,3,0을 누르면 된다.

# 그런데 얼마 전, 꿍은 알람시계를 맞추다가 시각을 잘못 입력했는데 화면에 나타나는 시간은 24로 나눈 나머지라는 것을 알게됐다. 마찬가지로 분 역시 60으로 나눈 나머지가 화면에 나타나는 사실을 알게됐다. 예를 들어 66:79로 시각을 잘못 입력했어도 실제로 화면에는 18:19로 나타난다는 것이다.

# 꿍은 매우 게을러서 원하는 알람시각을 맞추는데 최소한의 노력만 하고싶다. 그래서 여러분들은 꿍이 어떻게 하면 최소한의 노력을 들여서 원하는 시각으로 알람을 맞출 수 있을지 알아내는 프로그램을 만들어야 한다.



# 키보드는 위와 같이 생겼고 키 a에서 키 b로 이동할 때 필요한 노력은 다음과 같다.

# effort(a,b) = |xa-xb|+|ya-yb|

# 여기서 (xa, ya) 와 (xb, yb)는 키a, b의 좌표를 나타낸다.

# 전체 노력의 합은 첫 번째 키에서 두 번째 키로 이동하는데 필요한 노력, 두 번째 키에서 세 번째 키로 이동하는데 필요한 노력, 세 번째 키에서 네 번째 키로 이동하는데 필요한 노력의 세 값의 합으로 정의된다.

# 예를 들어 22:45를 입력하는데 필요한 전체 노력의 값은 effort(2,2)+effort(2,4)+effort(4,5)=0+2+1=3. 이다.

# 만약 답이 여러 가지라면 가장 빠른 시각을 출력하라.

li = []
a,b = input().split(':')
li.append((a,b))
a = int(a)
while True:
    a += 24
    if a >= 100:
        break
    else:
        li.append((str(a),b))
for i in range(len(li)):
    x,y = li[i]
    if int(y) <40:
        li.append((x,str(int(y)+60)))

ans = []
mi = 1000
ef = {}
ef[1] = (0,0)
ef[2] = (1,0)
ef[3] = (2,0)
ef[4] = (0,1)
ef[5] = (1,1)
ef[6] = (2,1)
ef[7] = (0,2)
ef[8] = (1,2)
ef[9] = (2,2)
ef[0] = (1,3)
while li:
    x,y = li.pop()
    a = int(x[0])
    b = int(x[1])
    c = int(y[0])
    d = int(y[1])
    t = (abs(ef[a][0]-ef[b][0]) + abs(ef[a][1]-ef[b][1]) + abs(ef[b][0]-ef[c][0]) + abs(ef[b][1]-ef[c][1]) 
         +abs(ef[d][0]-ef[c][0]) + abs(ef[d][1]-ef[c][1]))
    if t == mi:
        ans.append((x,y))
    if t < mi:
        ans = []
        ans.append((x,y))
        mi = t

a,b = ans[0]
x = a
y = b
a = int(a)
b = int(b)
b = b+a*60
while ans:
    m1,m2 = ans.pop()
    n1 = int(m1)
    n2 = int(m2)
    n2 = n2+n1*60
    if n2 < b:
        b = n2
        x = m1
        y = m2
print(x+':'+y)
    