#애너그램 만들기두 개의 영어 단어가 주어졌을 때, 두 단어가 서로 애너그램 관계에 있도록 만들기 위해서 제거해야 하는 최소 개수의 문자 수를 구하는 프로그램을 작성하시오. 
#문자를 제거할 때에는 아무 위치에 있는 문자든지 제거할 수 있다.

# 첫째 줄과 둘째 줄에 영어 단어가 소문자로 주어진다. 
# 각각의 길이는 1,000자를 넘지 않으며, 적어도 한 글자로 이루어진 단어가 주어진다.

import sys
a = sys.stdin.readline().rstrip()
b = sys.stdin.readline().rstrip()

lis1 = [0]*26
lis2 = [0]*26
for i in a:
    lis1[ord(i)-97]+=1

for j in b:
    lis2[ord(j)-97]+=1

ans = 0
for k in range(len(lis1)):
    if lis1[k]-lis2[k] > 0:
        ans += lis1[k]-lis2[k]
    else:
        ans += lis2[k] - lis1[k]
print(ans)