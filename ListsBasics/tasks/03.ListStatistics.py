n = int(input())

list_negative=[]
list_positive=[]

for i in range(n):
    num = int(input())
    if num>=0:
        list_positive.append(num)
    else:
        list_negative.append(num)

print(list_positive)
print(list_negative)
print(f"Count of positives: {len(list_positive)}\nSum of negatives: {sum(list_negative)}")