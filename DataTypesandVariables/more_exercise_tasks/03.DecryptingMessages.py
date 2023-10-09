key = int(input())
n=int(input())

word=""
for i in range(n):
    ch=input()
    num = ord(ch)
    word+=chr(num+key)

print(word)