n = int(input())

is_opened=False
is_balanced=True

for i in range(n):
    word=input()
    if is_opened==True and word[0]=="(":
        is_balanced=False
        break
    if is_opened==False and word[0]==")":
        is_balanced=False
        break
    if word[0]=="(":
        is_opened=True
        is_balanced=False
        continue
    if is_opened and word[0]==")":
        is_opened=False
        is_balanced=True
        continue

if is_balanced:
    print("BALANCED")
else:
    print("UNBALANCED")