# 다양한 단어란 모두 다른 알파벳 소문자로만 이루어진 단어를 의미한다. 
# 예를 들어, "codeplus", "coding", "algorithm"은 다양한 단어, "baekjoon", "startlink"는 다양한 단어가 아니다.

# 다양한 단어 S가 주어졌을 때, 사전 순으로 S의 바로 다음에 오는 다양한 단어를 구해보자.


word = input()

next = ''
for i in range(97,123):
    if chr(i) not in word:
        next = word+chr(i)
        break

if next:
    print(next)
else:
    last = word[-1]
    word = word[:-1]
    while len(word)>=1 and ord(word[-1]) > ord(last):
        last = word[-1]
        word = word[:-1]
    
    if len(word) == 0:
        print(-1)
    else:
        last = word[-1]
        word = word[:-1]
        for i in range(ord(last)+1,123):
            if chr(i) not in word:
                print(word+chr(i))
                break