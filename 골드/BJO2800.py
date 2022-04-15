# 어떤 수식이 주어졌을 때, 괄호를 제거해서 나올 수 있는 서로 다른 식의 개수를 계산하는 프로그램을 작성하시오.

# 이 수식은 괄호가 올바르게 쳐져 있다. 예를 들면, 1+2, (3+4), (3+4*(5+6))와 같은 식은 괄호가 서로 쌍이 맞으므로 올바른 식이다.

# 하지만, 1+(2*3, ((2+3)*4 와 같은 식은 쌍이 맞지 않는 괄호가 있으므로 올바른 식이 아니다.

# 괄호를 제거할 때는, 항상 쌍이 되는 괄호끼리 제거해야 한다.

# 예를들어 (2+(2*2)+2)에서 괄호를 제거하면, (2+2*2+2), 2+(2*2)+2, 2+2*2+2를 만들 수 있다. 하지만, (2+2*2)+2와 2+(2*2+2)는 만들 수 없다. 그 이유는 쌍이 되지 않는 괄호를 제거했기 때문이다.

# 어떤 식을 여러 쌍의 괄호가 감쌀 수 있다.

from itertools import combinations

mat = input()

l_pare = []
pare = []

for i in range(len(mat)):
    if mat[i] == '(':
        l_pare.append(i)
    elif mat[i] == ')':
        left = l_pare.pop()
        pare.append((left,i))

ans = []

for i in range(1,len(pare)+1):
    li = list(combinations(pare,i))
    for j in li:
        cnt = []
        for a,b in j:
            cnt.append(a)
            cnt.append(b)
        
        temp = ''
        for k in range(len(mat)):
            if k in cnt:
                continue
            else:
                temp += mat[k]
        ans.append(temp)


ans = set(ans)
ans = list(ans)
ans.sort()

for i in ans:
    print(i)