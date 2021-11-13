# N개의 자연수와 자연수 M이 주어졌을 때, 
# 아래 조건을 만족하는 길이가 M인 수열을 모두 구하는 프로그램을 작성하시오.

# N개의 자연수 중에서 M개를 고른 수열
# 입력
# 첫째 줄에 N과 M이 주어진다. (1 ≤ M ≤ N ≤ 8)

# 둘째 줄에 N개의 수가 주어진다. 입력으로 주어지는 수는 10,000보다 작거나 같은 자연수이다.


#재귀도 메모리값을 참조하기 때문에 append 하고 값을 바꾸면 리스트에 바뀐 값이 저장된다.
#따라서 deepcopy 방법을 쓰려 했으나 시간초과로 다른 방법을 찾았다.

#실패한 방법
# import sys
# from copy import deepcopy

# n,m = map(int,sys.stdin.readline().split())

# lis = sorted(map(int,sys.stdin.readline().split()))
# li = []
# check = []
# def func(k):
#     if k == m:
#         for i in range(m):
#             print(li[i],end=' ')
#         print()
#         check.append(deepcopy(li))
#         return
#     for j in range(n):
#         li.append(lis[j])
#         if li in check:
#             li.pop()
#             continue
#         func(k+1)
#         li.pop()


# func(0)


import sys

n,m = map(int,sys.stdin.readline().split())

lis = sorted(map(int,sys.stdin.readline().split()))
li = []
check = set()
che = [0]*10
def func(k):
    if k == m:
        ap = tuple(li)
        a = len(check)
        check.add(ap)
        if a != len(check):
            for i in range(len(li)):
                print(li[i],end=' ')
            print()
        return
    for j in range(n):
        if che[j] == 0:
            li.append(lis[j])
            che[j] = 1
            func(k+1)
            che[j] = 0
            li.pop()

func(0)

