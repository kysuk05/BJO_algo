# 이 문제는 아주 평범한 배낭에 관한 문제이다.

# 한 달 후면 국가의 부름을 받게 되는 준서는 여행을 가려고 한다. 
# 세상과의 단절을 슬퍼하며 최대한 즐기기 위한 여행이기 때문에, 가지고 다닐 배낭 또한 최대한 가치 있게 싸려고 한다.

# 준서가 여행에 필요하다고 생각하는 N개의 물건이 있다. 각 물건은 무게 W와 가치 V를 가지는데, 해당 물건을 배낭에 넣어서 가면 준서가 V만큼 즐길 수 있다. 
# 아직 행군을 해본 적이 없는 준서는 최대 K만큼의 무게만을 넣을 수 있는 배낭만 들고 다닐 수 있다. 준서가 최대한 즐거운 여행을 하기 위해 배낭에 넣을 수 있는 물건들의 가치의 최댓값을 알려주자.

# 입력
# 첫 줄에 물품의 수 N(1 ≤ N ≤ 100)과 준서가 버틸 수 있는 무게 K(1 ≤ K ≤ 100,000)가 주어진다. 
# 두 번째 줄부터 N개의 줄에 거쳐 각 물건의 무게 W(1 ≤ W ≤ 100,000)와 해당 물건의 가치 V(0 ≤ V ≤ 1,000)가 주어진다.


import sys
n,k = map(int,sys.stdin.readline().split())

li = []
for i in range(n):
    li.append(list(map(int,sys.stdin.readline().split())))

li.sort()
val = [0]*1001
stack = []
print(li)
for j in range(len(li)):
    w = li[j][0]
    v = li[j][1]
    if val[w] == 0:
        val[w] = v
    else:
        val[w] = max(val[w],v)
    for k in stack:
        sta = []
        if k[1] + v <= 1000:
            val[k[1]+v] = max(val[k[1]+v],k[0]+w)
            sta.append((k[0]+w,k[1]+v))
        else:
            continue
    
    for s in range(len(sta)):
        stack.append(sta[s][0],sta[s][1])
    stack.append((w,v))
print(max(val))
print(stack)