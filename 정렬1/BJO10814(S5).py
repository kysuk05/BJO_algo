# 첫째 줄에 온라인 저지 회원의 수 N이 주어진다. (1 ≤ N ≤ 100,000)

# 둘째 줄부터 N개의 줄에는 각 회원의 나이와 이름이 공백으로 구분되어 주어진다. 
# 나이는 1보다 크거나 같으며, 200보다 작거나 같은 정수이고, 이름은 알파벳 대소문자로 이루어져 있고, 길이가 100보다 작거나 같은 문자열이다. 
# 입력은 가입한 순서로 주어진다.

# 출력
# 첫째 줄부터 총 N개의 줄에 걸쳐 온라인 저지 회원을 나이 순, 나이가 같으면 가입한 순으로 한 줄에 한 명씩 나이와 이름을 공백으로 구분해 출력한다.

# 매핑 때 정렬하기 힘들어서 처음으로 사용해본 람다식
import sys

n = int(sys.stdin.readline())

li = []
for i in range(n):
    li.append(int(sys.stdin.readline().split()))

li.sort(key=lambda x: int(x[0]))

for i in range(len(li)):
    print(li[i][0],li[i][1])
    

#만약 람다식을 사용 안한다면?
import operator
li = []
for i in range(n):
    a,b = sys.stdin.readline().split()
    a = int(a)
    li.append((a,b))

li1 = sorted(li,key=operator.itemgetter(0))


for i in range(len(li1)):
    print(li1[i][0],li1[i][1])
    

