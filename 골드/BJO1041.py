# 주사위는 위와 같이 생겼다. 주사위의 여섯 면에는 수가 쓰여 있다. 위의 전개도를 수가 밖으로 나오게 접는다.

# A, B, C, D, E, F에 쓰여 있는 수가 주어진다.

# 지민이는 현재 동일한 주사위를 N3개 가지고 있다. 이 주사위를 적절히 회전시키고 쌓아서, N×N×N크기의 정육면체를 만들려고 한다. 이 정육면체는 탁자위에 있으므로, 5개의 면만 보인다.

# N과 주사위에 쓰여 있는 수가 주어질 때, 보이는 5개의 면에 쓰여 있는 수의 합의 최솟값을 출력하는 프로그램을 작성하시오.


n = int(input())
dice = list(map(int,input().split()))
d1 = min(dice)
d2 = 100
for i in range(6):
    for j in range(i+1,6):
        if i+j == 5:
            continue
        d2 = min(d2,dice[i]+dice[j])
d3 = 1000
for i in range(6):
    for j in range(i+1,6):
        for k in range(j+1,6):
            if i+j == 5 or j+k == 5 or i+k == 5:
                continue
            d3 = min(d3,dice[i]+dice[j]+dice[k])

dice.sort()

if n == 1:
    print(sum(dice[:5]))
elif n == 2:
    print(d2*4+d3*4)
else:
    ans = 0
    ans += ((n-2)**2)*5*dice[0]+((n-2)*4)*dice[0]
    ans += (((n-2)*8)+4)*d2
    ans += d3*4
    print(ans)