# 당신은 유명 프로그래밍 대회인 KCPC(Korean Collegiate Programming Contest)에 참가하고 있다. 이 대회에서 총 k개의 문제를 풀게 되는데, 어떤 문제에 대한 풀이를 서버에 제출하면 그 문제에 대해 0점에서 100점 사이의 점수를 얻는다. 풀이를 제출한 팀의 ID, 문제 번호, 점수가 서버의 로그에 제출되는 시간 순서대로 저장된다. 한 문제에 대한 풀이를 여러 번 제출할 수 있는데, 그 중 최고 점수가 그 문제에 대한 최종 점수가 된다. (만약 어떤 문제에 대해 풀이를 한번도 제출하지 않았으면 그 문제에 대한 최종 점수는 0점이다.) 

# 당신 팀의 최종 점수는 각 문제에 대해 받은 점수의 총합이고, 당신의 순위는 (당신 팀보다 높은 점수를 받은 팀의 수)+1 이다. 

# 점수가 동일한 팀이 여럿 있을 수 있는데, 그 경우에는 다음 규칙에 의해서 순위가 정해진다. 

# 최종 점수가 같은 경우, 풀이를 제출한 횟수가 적은 팀의 순위가 높다. 
# 최종 점수도 같고 제출 횟수도 같은 경우, 마지막 제출 시간이 더 빠른 팀의 순위가 높다. 
# 동시에 제출되는 풀이는 없고, 모든 팀이 적어도 한 번은 풀이를 제출한다고 가정하라. 

# 서버의 로그가 주어졌을 때, 당신 팀의 순위를 계산하는 프로그램을 작성하시오.

import sys

T = int(sys.stdin.readline())

for l in range(T):
    n,k,t,m = map(int,sys.stdin.readline().split())


    rank = [[[0,0,0]for i in range(k)]for i in range(n)]

    for _ in range(m):
        i,j,s = map(int,sys.stdin.readline().split())
        if rank[i-1][j-1][0] > -s:
            rank[i-1][j-1][0] = -s
        rank[i-1][j-1][1] += 1
        rank[i-1][j-1][2] = _

    score = []
    
    for i in rank:
        s1 = 0
        s2 = 0
        s3 = 0
        for j in i:
            s1 += j[0]
            s2 += j[1]
            s3 = max(s3,j[2])
        score.append((s1,s2,s3))
    ans = score[t-1]
    
    score.sort()
    
    for i in range(len(score)):
        if score[i] == ans:
            print(i+1)