# N과 L이 주어질 때, 합이 N이면서, 길이가 적어도 L인 가장 짧은 연속된 음이 아닌 정수 리스트를 구하는 프로그램을 작성하시오.



N,L = map(int,input().split())


while L<=100:
    t = ((2*N-L**2+L)/2)/L
    if t == int(t):
        break
    if t < 0:
        break
    L += 1


if t < 0 or L > 100:
    print(-1)
else:
    t = int(t)
    for i in range(L):
        print(t,end=' ')
        t += 1



