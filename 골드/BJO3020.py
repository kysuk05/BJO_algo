# 개똥벌레 한 마리가 장애물(석순과 종유석)로 가득찬 동굴에 들어갔다. 동굴의 길이는 N미터이고, 높이는 H미터이다. (N은 짝수) 첫 번째 장애물은 항상 석순이고, 그 다음에는 종유석과 석순이 번갈아가면서 등장한다.

# 아래 그림은 길이가 14미터이고 높이가 5미터인 동굴이다. (예제 그림)



# 이 개똥벌레는 장애물을 피하지 않는다. 자신이 지나갈 구간을 정한 다음 일직선으로 지나가면서 만나는 모든 장애물을 파괴한다.

# 위의 그림에서 4번째 구간으로 개똥벌레가 날아간다면 파괴해야하는 장애물의 수는 총 여덟개이다. (4번째 구간은 길이가 3인 석순과 길이가 4인 석순의 중간지점을 말한다)



# 하지만, 첫 번째 구간이나 다섯 번째 구간으로 날아간다면 개똥벌레는 장애물 일곱개만 파괴하면 된다.

# 동굴의 크기와 높이, 모든 장애물의 크기가 주어진다. 이때, 개똥벌레가 파괴해야하는 장애물의 최솟값과 그러한 구간이 총 몇 개 있는지 구하는 프로그램을 작성하시오.


import sys

N,H = map(int,sys.stdin.readline().split())

down = [0]*(H+1)
up = [0]*(H+1)


for i in range(N//2):
    down[int(sys.stdin.readline())]+=1
    up[H-int(sys.stdin.readline())+1]+=1


for i in range(H-1,0,-1):
    down[i] += down[i+1]

for i in range(1,H+1):
    up[i] += up[i-1]


min_num = 999999
num_range = 0
up[0] = 999999
for i in range(H+1):
    total_num = up[i] + down[i]
    if min_num > total_num:
        min_num = total_num
        num_range = 1
    elif min_num == total_num:
        num_range += 1

print(min_num,num_range)