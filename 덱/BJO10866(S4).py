# 정수를 저장하는 덱(Deque)를 구현한 다음, 입력으로 주어지는 명령을 처리하는 프로그램을 작성하시오.

# 명령은 총 여덟 가지이다.

# push_front X: 정수 X를 덱의 앞에 넣는다.
# push_back X: 정수 X를 덱의 뒤에 넣는다.
# pop_front: 덱의 가장 앞에 있는 수를 빼고, 그 수를 출력한다. 만약, 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
# pop_back: 덱의 가장 뒤에 있는 수를 빼고, 그 수를 출력한다. 만약, 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
# size: 덱에 들어있는 정수의 개수를 출력한다.
# empty: 덱이 비어있으면 1을, 아니면 0을 출력한다.
# front: 덱의 가장 앞에 있는 정수를 출력한다. 만약 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
# back: 덱의 가장 뒤에 있는 정수를 출력한다. 만약 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.

# 내가 구현했던 덱 들고오기


def push_front(num):
    deq[head] = num
def push_back(num):
    deq[tail] = num
def pop_front():
    print(deq[head])
def pop_back():
    print(deq[tail])
def front():
    print(deq[head])
def back():
    print(deq[tail-1])
def size():
    print(tail-head)
def empty():
    if tail==head:
        print(1)
    else:
        print(0)

import sys
ind = 10000
deq = [-1]*20000

head = ind
tail = ind

cnt = int(sys.stdin.readline())

for a in range(cnt):
    st = sys.stdin.readline().rstrip()
    if 'push_front' in st:
        a = st.split()
        head-=1
        push_front(int(a[1]))
    elif 'push_back' in st:
        a = st.split()
        push_back(int(a[1]))
        tail+=1
    elif 'size' in st:
        size()
    elif 'empty' in st:
        empty()
    elif 'pop_front' in st:
        if tail != head:
            pop_front()
            head+=1
        else:
            print(-1)
    elif 'pop_back' in st:
        if tail != head:
            tail-=1
            pop_back()
        else:
            print(-1)
    elif 'front' in st:
        if tail == head:
            print(-1)
        else: front()
    elif 'back' in st:
        if tail == head:
            print(-1)
        else: back()
