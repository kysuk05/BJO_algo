# 작년에 이어 새로운 문자열 게임이 있다. 게임의 진행 방식은 아래와 같다.

# 알파벳 소문자로 이루어진 문자열 W가 주어진다.
# 양의 정수 K가 주어진다.
# 어떤 문자를 정확히 K개를 포함하는 가장 짧은 연속 문자열의 길이를 구한다.
# 어떤 문자를 정확히 K개를 포함하고, 문자열의 첫 번째와 마지막 글자가 해당 문자로 같은 가장 긴 연속 문자열의 길이를 구한다.
# 위와 같은 방식으로 게임을 T회 진행한다.



import sys

T = int(sys.stdin.readline())

for i in range(T):
    alpha = [[]for _ in range(26)]
    word = sys.stdin.readline().rstrip()
    for j in range(len(word)):
        alpha[ord(word[j])-97].append(j)
    
    ans = -1
    
    K = int(sys.stdin.readline())

    min_word = 10001
    max_word = 0
    
    
    for j in range(26):
        if len(alpha[j]) >= K:
            for k in range(K-1,len(alpha[j])):
                min_word = min(min_word,alpha[j][k]-alpha[j][k-K+1]+1)
                max_word = max(max_word,alpha[j][k]-alpha[j][k-K+1]+1)
    
    if min_word == 10001 and max_word == 0:
        print(ans)
    else:
        print(min_word,max_word)