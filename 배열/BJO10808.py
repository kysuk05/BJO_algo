#알파벳 소문자로만 이루어진 단어 S가 주어진다. 각 알파벳이 단어에 몇 개가 포함되어 있는지 구하는 프로그램을 작성하시오.

word = input()
word_list = []
for a in word:
    word_list.append(ord(a))

list1 = [0] * 26

#아스키코드 사용
for num in range(len(word_list)):
    A = word_list[num]-97
    list1[A]+=1


for a in range(len(list1)):
    print(list1[a],end=' ')