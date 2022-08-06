# 흑석동은 최근 뉴타운 공사로 인하여 지나가면 안되는 위험 지역이 존재한다. 이 지역은 X축, Y축과 평행한 직사각형 형태로 이루어져 있다.

# 중앙대의 마스코트인 푸앙이는 직선 상의 경로를 따라서 흑석동을 통과하고 있다. 이 때 흑석동의 망령 호민이는 푸앙이가 위험지역에 지나갈 것 같다는 생각이 들었다. 따라서 푸앙이가 위험 지역을 지나가는지 여부를 알아내어서 푸앙이가 해당 지역을 지나가지 못하도록 조치를 취할 예정이다.

# 호민이를 위해 푸앙이가 위험 지역을 지나는 지 알려주는 프로그램을 작성해보자.

import sys

a,b,c = map(int,sys.stdin.readline().split())

x1,x2,y1,y2 = map(int,sys.stdin.readline().split())


ans = 'Lucky'
if a*b > 0:
    if (a*x1+b*y1+c)*(a*x2+b*y2+c) < 0:
        ans = 'Poor'
else:
    if (a*x2+b*y1+c)*(a*x1+b*y2+c) < 0:
        ans = 'Poor'
print(ans)