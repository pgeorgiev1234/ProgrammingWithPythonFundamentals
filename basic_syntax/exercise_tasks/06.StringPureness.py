n = int(input())

for i in range(n):
    word = input()
    for j in range(len(word)):
        if word[j]=="," or word[j]=="." or word[j]=="_":
            print(f"{word} is not pure!")
            break
    else:
        print(f"{word} is pure.")