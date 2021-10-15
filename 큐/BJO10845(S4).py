# 정수를 저장하는 큐를 구현한 다음, 입력으로 주어지는 명령을 처리하는 프로그램을 작성하시오.

# 명령은 총 여섯 가지이다.

# push X: 정수 X를 큐에 넣는 연산이다.
# pop: 큐에서 가장 앞에 있는 정수를 빼고, 그 수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
# size: 큐에 들어있는 정수의 개수를 출력한다.
# empty: 큐가 비어있으면 1, 아니면 0을 출력한다.
# front: 큐의 가장 앞에 있는 정수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
# back: 큐의 가장 뒤에 있는 정수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.

#내가 구현했던 큐 들고 오기

import sys
head = 0
tail = 0
que = []


def front():
    print(que[head])
def back():
    print(que[tail-1])
def pop():
    global head
    head +=1
def push(num):
    que.append(num)
    global tail
    tail +=1
def empty():
    if head == tail:
        print(1)
    else:
        print(0)
def size():
    print(tail-head)


cnt = int(sys.stdin.readline())

for a in range(cnt):
    st = sys.stdin.readline()
    if 'push' in st:
        a = st.split()
        push(int(a[1]))
    elif 'front' in st:
        if tail == head:
            print(-1)
        else:
            front()
    elif 'back' in st:
        if tail == head:
            print(-1)
        else:
            back()
    elif 'size' in st:
        size()
    elif 'empty' in st:
        empty()
    elif 'pop' in st:
        if head == tail:
            print(-1)
        else:
            front()
            pop()