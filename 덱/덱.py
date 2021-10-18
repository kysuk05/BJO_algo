# 직접 구현 한 큐. 하지만 파이썬에서는 이보다 효율적인 deque를 collection 라이브러리에서
# 지원한다. 실제로 사용할 때에는 라이브러리를 이용해서 구현할 것.
# 여기서는 배열을 이용해서 구현해본다는 것에 의미가 있다.


a = 1000000
deq = [-1]*2000000

head = a
tail = a

def push_front(num):
    global head
    deq[head] = num
    head -=1
def push_back(num):
    global tail
    deq[tail] = num
    tail +=1
def pop_front():
    global tail, head
    if tail != head:
        head+=1
def pop_back():
    global tail, head
    if tail != head:
        tail-=1
def front():
    if tail!= head:
        print(deq[head])
def back():
    if tail!= head:
        print(deq[tail])