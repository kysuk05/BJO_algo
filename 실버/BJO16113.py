# zxcvber는 외계인을 연구하는 과학자다. 그는 지난 10년간 우주에서 오는 시그널를 연구했지만, 아무런 성과가 없었다. 그러던 어느 날, 갑자기 우주에서 이상한 시그널이 오기 시작했다. zxcvber는 매우 기뻐하며 시그널을 받아서 분석해보았다. 시그널은 0과 1로 이루어져 있는데, 여기서는 편의상 0을 ".", 1을 "#"으로 표시한다. 시그널은 다음과 같았다.

# ###.....###.#..####.#.......#.#....####.....###.#....##.#.......#.#....####.....###.#....#

# 다른 여러 시그널들을 분석해본 결과, zxcvber는 시그널의 길이가 항상 5의 배수라는 것을 알게 되었다. 시그널을 다섯 개로 쪼개면 뭔가 규칙이 보이지 않을까 생각한 zxcvber는 시그널을 같은 길이의 5개의 시그널로 쪼갰다. 그러자 놀라운 일이 벌어졌다. 아래는 시그널을 쪼갠 뒤 "#"을 검은색, "."을 흰색으로 표시한 그림이다.



# 시그널은 디지털 숫자를 나타내고 있었다! 1-3열에 8, 9-11열에 3, 13열에 1, 그리고 16-18열에 7이 나타난 것이다. 이 숫자들이 특별한 의미를 갖고 있을 것이라 생각한 zxcvber는 다른 시그널들도 해독을 하기 시작했다. 하지만 시그널들의 길이가 너무 길어서, 일일히 손으로 확인하기에는 한계가 있었다. 다만, 짧은 시그널들을 분석하면서 zxcvber는 시그널의 규칙들을 파악할 수 있었다.

# 1. 시그널은 "."과 "#"으로 이루어져 있다.
# 2. 시그널을 해독한 결과에는 반드시 숫자가 1개 이상 있다.
# 3. 시그널에 등장하는 모든 "#"은 올바른 숫자 패턴에 포함되어 있다.
# 4. 숫자와 숫자 사이에는 1열 이상의 공백이 있다. 여기서 공백은, 열의 성분이 모두 "."인 열을 의미한다.
# 5. 0부터 9는 아래와 같이 나타난다. 역시 "#"을 검은색, "."을 흰색으로 표시했다.



# 주의할 점은, 1은 다른 숫자들과는 다르게 1열을 차지한다는 것이다. zxcvber를 도와 시그널을 해독해보자!

import sys


n = int(sys.stdin.readline())//5

sig = sys.stdin.readline().rstrip()

graph = []

for i in range(5):
    temp = []
    for j in range(n):
        temp.append(sig[i*n+j])
    temp.append('.')
    graph.append(temp)


idx = 0
ans = []
while idx < n+1:
    if graph[0][idx] != '#':
        idx += 1
        continue
    
    if graph[0][idx] == graph[1][idx] == graph[2][idx] == graph[3][idx] == graph[4][idx]:
        if graph[2][idx+1] == '#':
            if graph[1][idx+2] == '#':
                ans.append(8)
            else:
                ans.append(6)
            idx += 3
        elif graph[0][idx+1] == '#':
            ans.append(0)
            idx += 3
        else:
            ans.append(1)
            idx += 1
    elif graph[0][idx] == graph[1][idx]:
        if graph[0][idx+1] == '#':
            if graph[1][idx+2] == '#':
                ans.append(9)
            else:
                ans.append(5)
        else:
            ans.append(4)
        idx += 3
    elif graph[0][idx] == graph[2][idx]:
        if graph[3][idx] == '#':
            ans.append(2)
        else:
            ans.append(3)
        idx += 3
    else:
        ans.append(7)
        idx += 3
for i in ans:
    print(i,end='')
        