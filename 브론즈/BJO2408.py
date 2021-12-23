# 어떤 임의의 수식이 입력으로 들어올때 수식을 계산하는 프로그램을 짜시오. 수의 크기는 -10100 이상 10100이하이고, 수식에 괄호는 없다.

# 소수점이 나올 경우, 소수점은 내린다. 참고로, -5/2 = -3이고, 5/-2도 -3이다. -5/-2는 2이다.

# 입력
# 수의 개수 N(1 ≤ N ≤ 10) 이 주어지고 다음 2N-1 개의 줄에는 수와 연산자(+, -, *, /) 가 번갈아서 들어온다.

n = int(input())
li = []
for i in range(2*n-1):
    li.append(input())

st = [li[0]]

for j in range(2,len(li),2):
    if li[j-1] == "*":
        t = st.pop()
        st.append(int(t)*int(li[j]))
    elif li[j-1] == "/":
        t = st.pop()
        st.append(int(t)//int(li[j]))
    else:
        st.append(li[j-1])
        st.append(li[j])
ans = int(st[0])
for j in range(1,len(st)-1,2):
    if st[j] == "+":
        ans+=int(st[j+1])
    elif st[j] == "-":
        ans-=int(st[j+1])
print(ans)
    