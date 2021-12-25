# 2018년에 대한민국 평창에서 동계올림픽이 개최된다. 그 중에서도 스키는 동계올림픽의 꽃이지만 유독 우리나라에선 인기가 좀 없는 것 같다. 그래서 이번 평창올림픽에선 새로운 스키 경기 규칙이 적용 되었다. 새로 적용된 규칙은 다음과 같다.

# 스키 경기는 두 번의 경주로 이루어져 있다. 총 N명의 선수가 첫 번째 경주에 참가하고 각각 번호를 부여받는다. 1번 선수부터 N번 선수까지 순서대로 한 명씩 산을 타고 내려간다. 산을 다 내려오면 내려온 선수의 현재 순위가 정해질 것이다. 첫 번째 경주가 끝나고 난 뒤 최종적으로 정해진 순위에 따라서 1등부터 M등까지의 선수들에게만 두 번째 경주에 나갈 수 있는 자격이 주어진다. 

# 두 번째 경주에서는 첫 번째 경주에서 늦게 들어온 순서대로(M등부터 시작해서 1등까지) 한 명씩 산을 타고 내려간다. 산을 다 내려오면 내려온 선수의 현재 순위가 정해질 것이다. 두 번째 경주가 끝나고 난 뒤 최종적으로 정해진 순위에 따라서 1등, 2등 그리고 3등에게 각각 금메달, 은메달, 동메달이 수여 될 것이다.

# 이때 메달을 얻은 선수들의 번호를 구하는 프로그램을 작성해야 한다.(경주에 참가한 모든 선수들은 한 명도 빠짐없이 경주를 완주한다. 두 명 이상의 선수가 동시에 들어오는 경우는 없다.)


n,m = map(int,input().split())

li = []

for i in range(1,n+1):
    li.insert(int(input())-1,i)

lis = li[:m]
lis.reverse()
ans = []
for j in range(len(lis)):
    ans.insert(int(input())-1,lis[j])


for i in range(3):
    print(ans[i])