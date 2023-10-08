n = int(input())

sum = 0
for i in range(n):
    ch = input()
    sum+=ord(ch)

print(f"The sum equals: {sum}")