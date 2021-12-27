# Welcome to Zombieland! For the next five hours, your team will battle wits with hordes of the undead. Do you have the cunning, will, and stamina to survive? Follow the rules, and you may live to tell the tale.

# In Zombieland, there are a fundamental set of rules you must follow to stay alive. Rule 8 is “Get a kick&@% partner”, rule 18 is “Limber up”, rule 29 is “The buddy system”, and rule 22 is, “When in doubt, know your way out”.

# If you intend to survive for long in Zombieland, you’ll need to know which rule number goes with which quote. Write a program to display the correct quote given the rule number.

# Have fun during your stay in Zombieland, and remember rule 32, “Enjoy the little things”. 



import sys

n = int(sys.stdin.readline())

li = []

for i in range(n):
    li.append(sys.stdin.readline().rstrip())

t = int(sys.stdin.readline())

for j in range(t):
    m = int(sys.stdin.readline())
    if m-1 >= 0 and m-1 < len(li):
        print('Rule '+(str(m))+': '+li[m-1])
    else:
        print('Rule '+(str(m))+': '+'No such rule')
