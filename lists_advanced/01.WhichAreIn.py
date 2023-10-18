list1=input().split(", ")
list2=input().split(", ")

list3=[]

for word in list1:
    for word2 in list2:
        if word in word2:
            list3.append(word)
            break

print(list3)