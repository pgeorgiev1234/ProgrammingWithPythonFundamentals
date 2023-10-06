n = int(input())
total = 0

for i in range(n):
    price = float(input())
    days = int(input())
    caps_per_day= int(input())
    if price<0.01 or price>100.00 or days<1 or days>31 or caps_per_day<1 or caps_per_day>2000:
        continue
    else:
        smetka = price*days*caps_per_day
        print(f"The price for the coffee is: ${smetka:.2f}")
        total+=smetka

print(f"Total: ${total:.2f}")