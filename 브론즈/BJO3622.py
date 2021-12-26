# 대부분의 사람들은 잘 모르는 사실이지만 지구와 멀리 떨어지지 않은 별에는 지능이 있는 호박들이 모여 산다. 이 벌은 매우 똑똑하고, 여행을 즐긴다. 할로윈 연휴 시즌에 이 별에서 가장 인기있는 여행 코스는 지구를 방문하는 것이다.

# 호박은 지능을 가지고 있지만, 스스로 움직일 수 없다. 따라서, 호박은 연휴동안 자신을 도와줄 사람을 찾아야 한다. 이 과정은 아래와 같다.

# 먼저, 사람을 한 명 고른 다음, 특별한 생물학적 조작을 통해 호박 자신의 모습을 꾸미게 한다. 보통은 호박의 몸에 이런 저런 구멍을 내어 치장하고, 안에 촛불을 켠다.

# 사실, 할로윈은 호박별의 호박들이 즐기는 축제이다. 대부분의 사람은 할로윈의 거리에 울려 퍼지는 비명 소리의 절반 이상이 호박 외계인에 의한 것을 모른다는 사실을 보면, 딱히 대단한 반전은 아니다.

# 특별한 전송 장치가 있어야 위와 같은 생물학적 조작 과정을 거칠 수 있다. 전송 장치는 두 개의 금으로 만든 고리로 이루어져 있는데, 알 수 없는 이유 때문에 이 고리 두 개는 반드시 하나의 동일한 판으로부터 잘라내어야 한다. 고리의 크기는 호박의 특성을 나타내기 때문에, 호박마다 다르다. 다라서, 호박들은 지구에 첫 여행을 오기 전에 반드시 자신만의 고리를 만드는 작업을 해야 한다.

# 호박별의 외계인 진욱이는 방항 동안 편의점 아르바이트로 엄청난 돈을 모았고, 태어나서 처음으로 지구로 여행을 가려고 한다. 고리를 만들기 위한 금판을 구매한 진욱이는 이 금판으로부터 자신에게 꼭 맞는 두 개의 고리를 잘라낼 수 있는지 여부를 알고싶어 한다. 만약, 잘라낼 수 없는 경우에는 새 금판을 사기 위해 다시 편의점으로 돌아가야 하고, 영영 학교를 졸업할 수 없을 것이다.

A,a,B,b,P = map(int,input().split())

if A+B <= P:
    print('Yes')
elif A <= P and B <= P:
    if A<=b:
        print('Yes')
    elif B<=a:
        print('Yes')
    else:
        print('No')
else:
    print('No')