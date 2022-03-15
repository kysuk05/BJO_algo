# 수를 처리하는 것은 통계학에서 상당히 중요한 일이다. 통계학에서 N개의 수를 대표하는 기본 통계값에는 다음과 같은 것들이 있다. 단, N은 홀수라고 가정하자.

# 산술평균 : N개의 수들의 합을 N으로 나눈 값
# 중앙값 : N개의 수들을 증가하는 순서로 나열했을 경우 그 중앙에 위치하는 값
# 최빈값 : N개의 수들 중 가장 많이 나타나는 값
# 범위 : N개의 수들 중 최댓값과 최솟값의 차이
# N개의 수가 주어졌을 때, 네 가지 기본 통계값을 구하는 프로그램을 작성하시오.


from collections import Counter
import sys

n = int(sys.stdin.readline())


li = []
for i in range(n):
    li.append(int(sys.stdin.readline()))
li.sort()    

avg = round(sum(li)/n)

median = li[n//2]
max_mod = max(Counter(li).values())
mode_num = [i for i,j in Counter(li).items() if j == max_mod]



print(avg)
print(median)
if len(mode_num) >= 2:
    print(mode_num[1])
else:
    print(mode_num[0])

print(li[-1]-li[0])