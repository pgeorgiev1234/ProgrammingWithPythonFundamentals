numbers = [int(x) for x in input().split(", ")]

pos_numbers,neg_numbers,even,odd=[],[],[],[]

for num in numbers:
    if num>=0:
        pos_numbers.append(num)
    else:
        neg_numbers.append(num)

    if num%2==0:
        even.append(num)
    else:
        odd.append(num)
print(f"Positive: {', '.join(str(x) for x in pos_numbers)}\n"
      f"Negative: {', '.join(str(x) for x in neg_numbers)}\n"
      f"Even: {', '.join(str(x) for x in even)}\n"
      f"Odd: {', '.join(str(x) for x in odd)}")

