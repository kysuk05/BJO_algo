#큐 구현
import sys
head = 0
tail = 0
que = []


def fornt():
    print(que[head])
def back():
    print(que[tail])
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