

## 이렇게 구하니 시간초과...
# import sys
# a = int(sys.stdin.readline())
# lis1 = list(map(int,sys.stdin.readline().split()))
# b=[]
# for i in range(len(lis1)-1,0,-1):
#     for j in range(i-1,-1,-1):
#         if lis1[j]>lis1[i]:
#             b.append(lis1.index(lis1[j])+1)
#             break
#         elif j==0:
#             b.append(0)
#             break
# b.append(0)
# b.reverse()
# for k in range(len(b)):
#     print(b[k],end=' ')

# 이것도 시간초과
# import sys
# a = int(sys.stdin.readline())
# if a == 1:
#     b = int(sys.stdin.readline())
#     print(0)
# else:
#     b = list(map(int,sys.stdin.readline().split()))
#     max = b[0]
#     ans = []        
#     for i in range(len(b)):
#         if max <= b[i]:
#             ans.append(0)
#             max = b[i]
#         else:
#             for j in range(len(ans),-1,-1):
#                 if b[j] > b[i]:
#                     ans.append(b.index(b[j])+1)
#                     break
#     for i in range(len(ans)):
#         print(ans[i],end=' ')


# 시간초과(1)
# import sys
# a = int(sys.stdin.readline())
# if a == 1:
#     b = int(sys.stdin.readline())
#     print(0)
# else:
#     b = list(map(int,sys.stdin.readline().split()))
#     max = b[0]
#     stack = []
#     ans = []        
#     for i in range(a):
#         stack.append(b[i])
#         if max <= b[i]:
#             ans.append(0)
#             max = b[i]
#         else:
#             while stack[-2]<stack[-1]:
#                 stack.pop(-2)
#             ans.append(b.index(stack[-2])+1)
# print(ans)

#시간초과(2)
# import sys
# a = int(sys.stdin.readline())
# b = list(map(int,sys.stdin.readline().split()))
# stack = []
# ans = []        
# for i in range(a):
#     stack.append(b[i])
#     try:
#         while stack[-2]<stack[-1]:
#             stack.pop(-2)
#         ans.append(b.index(stack[-2])+1)
#     except:
#         ans.append(0)
        
# for i in range(len(ans)):            
#     print(ans[i],end=' ')

#시간초과(3)
# import sys
# a = int(sys.stdin.readline())
# b = list(map(int,sys.stdin.readline().split()))
# stack = []
# ans = []
# max = b[0]        
# for i in range(a):
#     if i == 0:
#         stack.append(b[i])
#         ans.append(0)
#     else:
#         k = stack.pop()
#         if b[i] > max:
#             max = b[i]
#             stack.append(b[i])
#             ans.append(0)
#         elif b[i] > k:
#             while k<b[i]:
#                 k = stack.pop()
#             stack.append(k)
#             stack.append(b[i])
#             ans.append(b.index(k)+1)
#         else:
#             stack.append(k)
#             stack.append(b[i])
#             ans.append(b.index(k)+1)
# print(ans)



# 드디어 찾은 풀이... index()가 시간복잡도가 O(N)이라는 말을 듣고
# index를 저장할 ind를 따로 만들어서 pop과 append로만 저장, 관리 하는데..
# 코드가 좀 더럽다.
# import sys
# a = int(sys.stdin.readline())
# b = list(map(int,sys.stdin.readline().split()))
# stack = []
# ans = []
# max = b[0]
# ind = []        
# for i in range(a):
#     if i == 0:
#         stack.append(b[i])
#         ind.append(i)
#         ans.append(0)
#     else:
#         k = stack.pop()
#         if b[i] > max:
#             max = b[i]
#             stack.append(b[i])
#             ind.append(i)
#             ans.append(0)
#         elif b[i] > k:
#             while k<b[i]:
#                 k = stack.pop()
#                 num = ind.pop()
#             stack.append(k)
#             stack.append(b[i])
#             ans.append(ind[-1]+1)
#             ind.append(i)
#         else:
#             stack.append(k)
#             stack.append(b[i])
#             ans.append(ind[-1]+1)
#             ind.append(i)

# for k in ans:
#     print(ans[k],end=' ')



# 몇번의 수정 끝에 완성한 코드    
import sys
a = int(sys.stdin.readline())
b = list(map(int,sys.stdin.readline().split()))
ind = []  
ans = []
for i in range(0,a):
    while ind and (b[ind[-1]] < b[i]):
        ind.pop()
    if len(ind)>0:
        ans.append(ind[-1]+1)
    else:
        ans.append(0)
    ind.append(i)

    
for i in range(len(ans)):
    print(ans[i],end=' ')
