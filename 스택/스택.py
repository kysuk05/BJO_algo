import sys
index = 0
sta = []

def top():
    print(sta[-1])
def pop():
    print(sta.pop(index-1))
def push(num):
    sta.append(num)
def empty():
    if index == 0:
        print(1)
    else:
        print(0)
def size():
    print(index)