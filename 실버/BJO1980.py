# 민혁이는 타워버거와 불고기버거를 매우 좋아한다. 민혁이는 타워버거를 먹는데 n분이 걸리고, 불고기버거를 먹는데 m분이 걸린다. 그는 t분 동안 햄버거를 최대한 많이 먹으려고 한다. 햄버거를 먹는 도중에 t분이 끝나면 안 되고, 아무것도 안 먹고 있을 때는 콜라를 마신다. 문제의 목적은 다음과 같다.

# 우선 콜라를 마시는 시간을 최소로 한다.
# 콜라를 마시는 시간이 같은 여러 가지 경우에는 햄버거를 가장 많이 먹을 수 있는 경우를 알아본다.
# 입력
# 첫 줄에 n, m, 주어진 시간 t가 주어진다. 세 수는 모두 1만 이하의 자연수이다.


n,m,t = map(int, input().split())

x = min(n,m)
y = max(n,m)

sta = []
if t % x == 0:
    sta.append((0,t//x))
else:
    sta.append((t%x,t//x))
    nu1 = t%x
    nu2 = t-nu1
    while nu2 > 0:
        nu1 += x
        nu2 -= x
        if nu1-y < 0:
            continue
        else:
            nu1-=y
            if nu1 == 0:
                sta.append((nu1,nu2//x+(t-nu2)//y))
                break
            else:
                sta.append((nu1,nu2//x+(t-nu2)//y))

sta.sort(key = lambda x : x[0])
print(sta[0][1],sta[0][0])