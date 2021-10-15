# 과거 이집트인들은 각 변들의 길이가 3, 4, 5인 삼각형이 직각 삼각형인것을 알아냈다.
# 주어진 세변의 길이로 삼각형이 직각인지 아닌지 구분하시오.
# 각 입력에 대해 직각 삼각형이 맞다면 "right", 아니라면 "wrong"을 출력한다.


while True:
    lis = list(map(int,input().split()))
    if lis[0]==0 and lis[1]==0 and lis[2]==0:
        break
    else:
        mnum = lis.pop(lis.index(max(lis)))
        if mnum**2 == lis[0]**2 + lis[1]**2:
            print('right')
        else:
            print('wrong')