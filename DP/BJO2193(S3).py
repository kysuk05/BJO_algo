ans = [1,1,2]

n = int(input())

if n <= len(ans):
    print(ans[n-1])
else:
    for i in range(4,n+1):
        ans.append(ans[i-3]+ans[i-2])

    print(ans[-1])