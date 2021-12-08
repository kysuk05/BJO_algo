# 입력 데이터는 표준입력을 사용한다. 입력은 T개의 테스트 데이터로 구성된다. 입력의 첫 번째 줄에는 입력 데이터의 수를 나타내는 정수 T가 주어진다. 각 테스트 데이터의 첫째 줄에는 Q에 적용할 연산의 개수를 나타내는 정수 k (k ≤ 1,000,000)가 주어진다. 이어지는 k 줄 각각엔 연산을 나타내는 문자(‘D’ 또는 ‘I’)와 정수 n이 주어진다. ‘I n’은 정수 n을 Q에 삽입하는 연산을 의미한다. 동일한 정수가 삽입될 수 있음을 참고하기 바란다. ‘D 1’는 Q에서 최댓값을 삭제하는 연산을 의미하며, ‘D -1’는 Q 에서 최솟값을 삭제하는 연산을 의미한다. 최댓값(최솟값)을 삭제하는 연산에서 최댓값(최솟값)이 둘 이상인 경우, 하나만 삭제됨을 유념하기 바란다.

# 만약 Q가 비어있는데 적용할 연산이 ‘D’라면 이 연산은 무시해도 좋다. Q에 저장될 모든 정수는 32-비트 정수이다. 

# 출력
# 출력은 표준출력을 사용한다. 각 테스트 데이터에 대해, 모든 연산을 처리한 후 Q에 남아 있는 값 중 최댓값과 최솟값을 출력하라. 두 값은 한 줄에 출력하되 하나의 공백으로 구분하라. 만약 Q가 비어있다면 ‘EMPTY’를 출력하라.

# heapq에서 최댓값 최솟값을 동시에 지원하지 않아 직접 구현
import sys
import heapq

n = int(sys.stdin.readline())
for i in range(n):
    mli = []
    nli = []
    graph = {}
    t = int(sys.stdin.readline())
    for j in range(t):
        co,nu = map(str,sys.stdin.readline().split())
        nu = int(nu)
        if co == 'I':
            heapq.heappush(mli,-nu)
            heapq.heappush(nli,nu)
            if nu in graph:
                graph[nu] +=1
            else:
                graph[nu] = 1
        else:
            if graph:
                if nu == 1:
                    k = -heapq.heappop(mli)
                    if k not in graph:
                        while k not in graph:
                            k = -heapq.heappop(mli)
                else:
                    k = heapq.heappop(nli)
                    if k not in graph:
                        while k not in graph:
                            k = heapq.heappop(nli)
                graph[k] -= 1
                if graph[k] == 0:
                    graph.pop(k)
    if graph:
        print(max(graph.keys()),min(graph.keys()))
    else:
        print('EMPTY')