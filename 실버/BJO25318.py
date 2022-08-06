# solved.ac는 프로그래밍 문제해결 사이트 백준 온라인 저지에 있는 문제들에 난이도를 붙이는 커뮤니티 프로젝트다. 기존에는 백준 온라인 저지의 문제들에 난이도 표기가 없어서, 다양한 문제를 풀어 보고 싶더라도 난이도를 가늠하기 어려워 무슨 문제를 풀어야 할지 판단하기 곤란했기 때문에 만들어졌다. solved.ac가 생긴 이후 $1\, 900$명 이상의 기여자 분들께서 소중한 난이도 의견을 공유해 주셨고, 지금은 약 $16\, 000$문제에 난이도가 붙게 되었다.

# 어떤 문제의 난이도는 그 문제를 푼 사람들이 제출한 난이도 의견을 바탕으로 결정한다. 기존에는 의견이 제출된 시점과 상관 없이 단순 절사평균으로 난이도를 결정했으나, 프로그래밍 문제 해결은 빠르게 변하는 분야이기 때문에 solved.ac는 새로운 의견들을 더 무겁게 반영하고자 난이도 산정 공식을 바꾸기로 했다. 어떤 문제에 $N$개의 난이도 의견이 제출되었을 때 문제의 난이도는 아래와 같은 방법으로 결정한다.

# 난이도 의견이 하나도 없다면 문제의 난이도는 $0$으로 한다.
# 난이도 의견이 하나 이상 있는 경우, 의견들을 제출한 시각에 따라 정렬한 뒤 각 의견의 가중치 $p_i$를 다음 수식으로 결정한다.
# 일
# \[p_i=\max\left( 0.5^{\left( t_N-t_i \right) /365\text{일}},0.9^{N-i} \right)\]
#  $t_i$는 $i$번째 난이도 의견이 제출된 시각을 의미한다. 시간 순으로 정렬했으므로 $t_1\le t_2\le\cdots\le t_N$이며, $t_N$은 가장 최근 제출된 의견의 제출 시각이 된다.
# 문제의 난이도 $X$는 $p_i$를 가중치로 갖는 가중평균을 소수점 아래 첫 번째 자리에서 반올림해 정수로 나타낸 것이다.
 
 
# \[X=\frac{p_1l_1+p_2l_2+\cdots +p_Nl_N}{p_1+p_2+\cdots +p_N} =\frac{\sum_{i=1}^{N}p_il_i}{\sum_{i=1}^{N}p_i}\]
#  $l_i$는 $i$번째 의견에 담긴 난이도를 $1$ 이상 $30$ 이하의 정수로 바꾼 값이다. $1$은 가장 낮은 난이도인 브론즈 $5$를, $30$은 가장 높은 난이도인 루비 $1$을 가리킨다.
# 사용자들이 어떤 문제에 제출한 난이도 의견 목록이 주어질 때, solved.ac가 결정한 문제의 난이도를 계산하는 프로그램을 작성하시오.


import sys

def roundup(num):
    if num - int(num) >= 0.5:
        return int(num) + 1
    else:
        return int(num)

n = int(sys.stdin.readline())

date = []
if n != 0:
    for i in range(n):
        day,time,score = sys.stdin.readline().split()
        
        year,month,days = map(int,day.split('/'))
        
        hour,min,sec = map(int,time.split(':'))
        
        temp = [year,month,days,hour,min,sec,int(score)]
        date.append(temp)

    y,m,d,h,mi,se,sc = date[-1]

    mon = [0,31,59,90,120,151,181,212,243,273,304,334,365]
    ps = []
    for i in range(len(date)):
        year,month,days,hour,min,sec,score = date[i]
        
        temp = ((((y-year)*365+mon[m-1]-mon[month-1]+d-days)*24+h-hour)*60+mi-min)*60+se-sec
        
        if ((year == 2020 and month <= 2 and days <= 29) or year < 2020) and ((y == 2020 and m >=3) or y > 2020):
            temp += 86400
        
        temp /= 31536000
        
        p = max(0.5**temp,0.9**(len(date)-1-i))
        ps.append(p)

    ans = 0
    for i in range(len(ps)):
        ans += ps[i]*date[i][-1]
    print(roundup(ans/sum(ps)))
else:
    print(0)