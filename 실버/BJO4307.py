# 개미 여러 마리가 길이가 lcm인 막대 위에 있다. 각 개미의 이동 속도는 모두 일정하며, 1cm/s이다. 개미가 막대의 마지막까지 걸어간다면, 개미는 그 즉시 떨어지게 된다. 또, 두 개미가 만나게 된다면, 방향을 반대로 바꾸어 걸어가게 된다.

# 가장 처음에 막대 상에서 개미의 위치를 알고 있다. 하지만, 개미가 어느 방향으로 움직이는 지는 알 수가 없다. 이때, 모든 개미가 땅으로 떨어질 때까지 가능한 시간 중 가장 빠른 시간과 느린 시간을 구하는 프로그램을 작성하시오.


import sys

n = int(sys.stdin.readline())


for i in range(n):
    late = 0
    early = 0
    stick,ants = map(int,sys.stdin.readline().split())
    mid = stick/2
    for j in range(ants):
        ant = int(sys.stdin.readline())
        if ant > mid:
            early = max(early,stick-ant)
            late = max(late,ant)
        else:
            early = max(early,ant)
            late = max(late,stick-ant)
    print(early,late)