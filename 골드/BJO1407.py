# 자연수 N이 주어지면, 자연수를 유지하면서 N을 2로 몇 번까지 나눌 수 있는지를 생각해 볼 수 있다. 즉, N의 모든 약수 중 2의 거듭제곱 꼴이면서 가장 큰 약수를 생각하는 것이다. 예를 들어 15의 경우는 2로 한 번도 나눌 수 없으므로 2^0 = 1이 해당되고, 40의 경우는 2로 세 번까지 나눌 수 있으므로 2^3 = 8이 해당된다. 이러한 약수를 함수값으로 가지는 함수 f(x)를 정의하자. 즉, f(15) = 1이고, f(40) = 8이다.

# 두 자연수 A, B(A≤B)가 주어지면, A 이상 B 이하의 모든 자연수에 대해서, 그 자연수의 모든 약수 중 2의 거듭제곱 꼴이면서 가장 큰 약수들의 총 합을 구하는 프로그램을 작성하시오. 즉 아래와 같은 수식의 값을 구해야 한다.

# f(A) + f(A+1) + ... + f(B-1) + f(B)


n,m = map(int,input().split())


m_arr = []
while m != 0:
    m_arr.append(m)
    m = m//2

n-= 1
n_arr = []
while n!= 0:
    n_arr.append(n)
    n = n//2

m_ans = 0
if len(m_arr) >= 2:
    for i in range(len(m_arr)-1):
        m_arr[i] = m_arr[i]-m_arr[i+1]
        m_ans += m_arr[i]*2**i
    m_ans += m_arr[-1]*2**(i+1)
else:
    m_ans = 1

n_ans = 0
if len(n_arr) >= 1:
    for i in range(len(n_arr)-1):
        n_arr[i] = n_arr[i]-n_arr[i+1]
        n_ans += n_arr[i]*2**i
    n_ans += n_arr[-1]*2**(i+1)
else:
    n_ans = 0


print(m_ans-n_ans)