# "The quick brown fox jumped over the lazy dogs."

# 이 문장은 모든 알파벳이 적어도 한 번은 나오는 문장으로 유명하다. 즉 26개의 서로 다른 문자를 갖고 있는 것이다.

# 각 케이스마다 문장에서 공백, 숫자, 특수 문자를 제외하고 얼마나 다양한 알파벳이 나왔는지를 구하면 된다. 대소문자는 하나의 문자로 처리한다. ex) 'A' == 'a'



import sys

while True:
    t = sys.stdin.readline().rstrip()
    if t == '#':
        break
    t = t.upper()
    di = {}
    for i in t:
        if ord(i) <=90 and ord(i) >= 65:
            di[i] = 0
    print(len(di))