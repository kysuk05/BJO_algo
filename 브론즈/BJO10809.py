# 알파벳 소문자로만 이루어진 단어 S가 주어진다. 각각의 알파벳에 대해서, 단어에 포함되어 있는 경우에는 처음 등장하는 위치를, 포함되어 있지 않은 경우에는 -1을 출력하는 프로그램을 작성하시오.

lis1 = [-1]*26

a = input()
ind = 0
for i in a:
    if lis1[ord(i)-97] == -1:
        lis1[ord(i)-97] = ind
    ind += 1


for j in range(len(lis1)):
    print(lis1[j],end=' ')