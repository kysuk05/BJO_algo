# A hotel has N rooms with two beds, numbered with numbers from 1 to N.

# When a group of guests arrive, they are accommodated in the following way: While there are empty rooms, each pair of guests is accommodated in an empty room with lowest number. If there is odd number of guests in a group then the last person will be accommodated alone in an empty room with lowest number. If there are no more empty rooms, then each guest is accommodated in a room with lowest number occupied by one guest, i.e. together with a guest from some other group.

# The hotel is initially empty. The order of arrivals of groups is known in advance. Write a program that will determine how many guests there will be in every room after last of them is accommodated.


n,m = map(int,input().split())

graph = [0]*n
for i in range(m):
    n = int(input())
    for j in range(len(graph)):
        if graph[j] == 0:
            if n > 2:
                graph[j] = 2
                n -= 2
            else:
                graph[j] = n
                n = 0
    
    if n != 0:
        for j in range(len(graph)):
            if graph[j] == 1:
                graph[j] += 1
                n -= 1
            if n == 0:
                break

for i in range(len(graph)):
    print(graph[i])