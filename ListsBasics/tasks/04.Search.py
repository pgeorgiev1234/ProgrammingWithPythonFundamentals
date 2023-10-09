n = int(input())
word = input()

list1 = []
list2 = []

for i in range(n):
    sentence = input()
    if word in sentence:
        list2.append(sentence)
    list1.append(sentence)

print(list1)
print(list2)