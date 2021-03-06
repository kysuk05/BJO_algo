# 앨버타의 자동차 번호판은 ABC-0123 (세 글자, 네 숫자)와 같이 두 부분으로 나누어져 있다.

# 좋은 번호판은 첫 번째 부분의 가치와 두 번째 부분의 가치의 차이가 100을 넘지 않는 번호판이다.

# 글자로 이루어진 첫 번째 부분의 가치는 글자를 26진법 수처럼 계산한다. (각 자리가 [A..Z]) 예를 들어, "ABC"의 가치는 28 (0×262 + 1×261 + 2×260)이 된다. "ABC-0123"은  |28 - 123| ≤ 100 이기 때문에, 좋은 번호판이다.

# 자동차 번호판이 주어졌을 때, 좋은 번호판인지 아닌지를 구하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 번호판의 수 N (1 ≤ N ≤ 100)이 주어진다. 다음 N개 줄에는 자동차 번호판이 LLL-DDDD 형식으로 주어진다.


k = int(input())

for i in range(k):
    s = input().split('-')
    an1 = (ord(s[0][0])-65)*(26**2)+(ord(s[0][1])-65)*(26**1)+(ord(s[0][2])-65)*(26**0)
    an2 = int(s[1])
    if abs(an1-an2) <= 100:
        print('nice')
    else:
        print('not nice')