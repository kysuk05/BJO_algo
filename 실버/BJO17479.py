# 2019년 1학기가 시작되고 많은 사람을 만나며 밥과 술에 탕진을 해버린 영기는 2학기에 탕진할 돈을 마련하기 위해 중앙대 근처의 고급 레스토랑, "정식당"에서 알바를 하게 되었다.

# 정식당의 사장 정우는 새로 들어온 알바생 영기를 위해 정식당만의 특별한 음식 주문법을 알려주려고 한다.

# 정식당에는 다양한 메뉴들이 있지만 크게 3가지로 나눌 수 있는데 A개의 "일반메뉴", B개의 "특별메뉴", C개의 "서비스메뉴"로 나뉘어져 있다. 일반메뉴는 자유롭게 주문할 수 있으나 특별메뉴와 서비스메뉴는 주문할 때 다음의 제약이 있다.

# 특별메뉴는 일반메뉴에서 총 20,000원 이상을 주문해야 주문할 수 있다.
# 서비스메뉴는 일반메뉴와 특별메뉴에서 총 50,000원 이상을 주문해야 주문할 수 있다.
# 서비스메뉴는 단 하나만 주문할 수 있다.
# 다양한 메뉴와 특별한 메뉴 주문법에 영기는 알바를 하면서 혼돈이 오기 시작했다. 받아서는 안될 주문을 받기도 하며 사장님에게 된통 혼나기도 하며 심지어는 자기 발에 걸려 넘어지기까지 했다.

# 가게를 찾아온 손님들이 주문하는 것이 옳은 주문인지 아닌지 헷갈려하는 영기는 우리에게 도움을 요청했다. 영기가 주문을 잘 받아올 수 있도록 우리가 도와주자.

import sys

nomal = {}
special = {}
service = {}

no,sp,se = map(int,sys.stdin.readline().split())

for i in range(no):
    no_name,no_num = sys.stdin.readline().split()
    nomal[no_name] = int(no_num)

for i in range(sp):
    sp_name,sp_num = sys.stdin.readline().split()
    special[sp_name] = int(sp_num)

for i in range(se):
    ser_name = sys.stdin.readline().rstrip()
    service[ser_name] = 1


t = int(sys.stdin.readline())

nm = 0
spm = 0
sem = 0


for i in range(t):
    menu = sys.stdin.readline().rstrip()
    if menu in nomal:
        nm += nomal[menu]
    elif menu in special:
        spm += special[menu]
    else:
        sem += service[menu]
ans = 'Okay'
if sem >= 2:
    ans = 'No'
elif sem == 1:
    if nm + spm < 50000:
        ans = 'No'
if spm != 0:
    if nm < 20000:
        ans = 'No'
print(ans)
        
    