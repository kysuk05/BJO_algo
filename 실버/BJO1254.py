# 동호와 규완이는 212호에서 문자열에 대해 공부하고 있다. 규완이는 팰린드롬을 엄청나게 좋아한다. 팰린드롬이란 앞에서부터 읽으나 뒤에서부터 읽으나 같게 읽히는 문자열을 말한다.

# 동호는 규완이를 위한 깜짝 선물을 준비했다. 동호는 규완이가 적어놓고 간 문자열 S에 0개 이상의 문자를 문자열 뒤에 추가해서 팰린드롬을 만들려고 한다. 동호는 가능하면 가장 짧은 문자열을 만들려고 한다.

# 동호가 만들 수 있는 가장 짧은 팰린드롬의 길이를 출력하는 프로그램을 작성하시오.


n = input()


for i in range(len(n)//2,len(n)):
    word = n[i:]
    leng = len(word)
    fel1 = n[i-leng:i]
    fel1 = fel1[::-1]
    fel2 = n[i-leng+1:i+1]
    fel2 = fel2[::-1]
    
    if word == fel1:
        print(len(n)*2-leng*2)
        break
    
    elif word == fel2:
        print(len(n)*2-leng*2+1)
        break