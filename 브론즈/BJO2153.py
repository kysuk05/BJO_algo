# 소수란 1과 자기 자신으로만 나누어떨어지는 수를 말한다. 예를 들면 1, 2, 3, 5, 17, 101, 10007 등이 소수이다. 이 문제에서는 편의상 1도 소수로 하자.

# 알파벳 대소문자로 이루어진 영어 단어가 하나 있을 때, a를 1로, b를 2로, …, z를 26으로, A를 27로, …, Z를 52로 하여 그 합을 구한다. 예를 들어 cyworld는 합을 구하면 100이 되고, abcd는 10이 된다.

# 이와 같이 구한 수가 소수인 경우, 그 단어를 소수 단어라고 한다. 단어가 주어졌을 때, 그 단어가 소수 단어인지 판별하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 단어가 주어진다. 단어의 길이는 20자 이하이다. 주어지는 단어는 알파벳 소문자와 대문자만으로 이루어져 있다.

# 출력
# 아래의 예제와 같은 형식으로 출력을 한다. 소수 단어인 경우에는 It is a prime word.를, 아닌 경우에는 It is not a prime word.를 출력한다.


t = input()
su = 0
for i in t:
    k = ord(i)
    if k > 96:
        k -= 96
    else:
        k -= 38
    su += k

if su == 1 or su == 2:
    print("It is a prime word.")
else:
    check = 0
    for i in range(2,su):
        if su%i == 0:
            check = 1
    if check == 1:
        print("It is not a prime word.")
    else:
        print("It is a prime word.")