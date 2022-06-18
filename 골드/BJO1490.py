# 어떤 수 N이 주어졌을 때, N으로 시작하면서, N의 0이 아닌 모든 자리수로 나누어지는 떨어지는 수 중 가장 작은 수를 출력하는 프로그램을 작성하시오.

n = input()

ans = n

for i in n:
    if int(i) == 0:
        continue
    if int(n)%int(i) != 0:
        ans = -1

if ans != -1:
    print(n)
else:
    add_num = ['0']
    while ans == -1:
        ans = n+''.join(add_num)
        for i in n:
            if int(i) == 0:
                continue
            if int(ans)%int(i) != 0:
                ans = -1
                break
        if int(add_num[-1]) != 9:
            temp = int(add_num.pop())
            temp += 1
            add_num.append(str(temp))
        else:
            up_num = 1
            re_list = []
            while add_num:
                temp = add_num.pop()
                if int(temp) == 9 and up_num == 1:
                    re_list.append('0')
                elif up_num == 1:
                    re_list.append(str(int(temp)+1))
                    up_num = 0
                else:
                    re_list.append(temp)
            if up_num == 1:
                re_list.append('0')
            re_list.reverse()
            add_num = re_list
    print(ans)