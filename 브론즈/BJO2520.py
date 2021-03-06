# 오늘은 내가 팬케이크 요리사!

# 은주는 팬케이크를 만들기로 했다. 은주 앞에는 지금 재료들이 있다. 이 재료들을 보고 있자니, 팬케이크를 최대 몇 개나 만들 수 있을지 궁금해졌다.

# 팬케이크를 만들기 위해서는 먼저 반죽을 해야 한다. 우유 8컵, 계란 노른자 8개, 설탕 4스푼, 소금 1스푼, 밀가루 9컵이 있으면 팬케이크 반죽 16개를 만들 수 있다. 어떤 0 이상의 실수 x에 대해 모든 재료가 앞에 주어진 양의 x배 이상 있다면 은주는 ⌊16x⌋개의 반죽을 만들 수 있다.

# 그 다음 반죽에 토핑을 얹고 구우면 팬케이크가 만들어진다. 은주가 만들 수 있는 팬케이크의 종류와 각각에 필요한 토핑의 목록은 다음과 같다.

# 바나나 팬케이크: 바나나 1개
# 딸기 팬케이크: 딸기잼 30그램
# 초콜릿 팬케이크: 초콜릿 스프레드 25그램
# 호두 팬케이크: 호두 10개
# 바나나는 여러 조각으로 나누거나 여러 조각을 합쳐서 사용할 수 있다. 예를 들어 1/3 크기의 바나나 조각이 3개 있으면 하나로 합쳐서 바나나 팬케이크를 만들 수 있다.

# 은주가 가지고 있는 재료들의 양이 주어졌을 때, 만들 수 있는 팬케이크의 최대 개수를 구하는 프로그램을 작성하시오.



import sys

n = int(sys.stdin.readline())
for i in range(n):
    t = sys.stdin.readline()
    a,b,c,d,e = map(int,sys.stdin.readline().split())
    t1 = min(int(a/8*16),int(b/8*16),int(c/4*16),int(d/1*16),int(e/9*16))

    w,x,y,z = map(int,sys.stdin.readline().split())
    t2 = (w//1+x//30+y//25+z//10)

    print(min(t1,t2))