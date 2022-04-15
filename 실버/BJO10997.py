# 예제를 보고 규칙을 유추한 뒤에 별을 찍어 보세요.


n = int(input())

if n == 1:
    print('*')
else:
    num = (n*4)-3
    print('*'*num)
    print('*')
    
    arr = [['*'for i in range(num)]for j in range(num)]
    dx = [0,1,0,-1]
    dy = [1,0,-1,0]
    
    x,y,i = 1,0,0
    
    
    while True:
        if x == n*2-1 and y == n*2-3:
            arr[y][x] = ' '
            break
        else:
            arr[y][x] = ' '
            if i == 0:
                if y+2 >= num or arr[y+2][x] == ' ':
                    i+=1
                else:
                    y+=1
            elif i == 1:
                if x+2 >= num or arr[y][x+2] == ' ':
                    i+=1
                else:
                    x+=1
            elif i == 2:
                if y-2 < 0 or arr[y-2][x] == ' ':
                    i+=1
                else:
                    y-=1
            else:
                if x-2 < 0 or arr[y][x-2] == ' ':
                    i-=3
                else:
                    x-=1
    for i in range(num):
        for j in range(num):
            print(arr[i][j],end='')
        print()
        
                    
    