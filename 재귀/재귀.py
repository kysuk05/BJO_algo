# n부터 1까지를 출력하는 재귀 함수
def re(n):
    if n == 0:
        return
    else:
        print(n)
        re(n-1)


a = int(input())
re(a)


# 1부터 N까지의 합을 출력하는 재귀함수
def add(num):
    if num == 0:
        return 0
    else: return num+add(num-1)

b = int(input())
print(add(b))
