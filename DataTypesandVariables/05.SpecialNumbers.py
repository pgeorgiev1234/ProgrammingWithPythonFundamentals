n = int(input())

for i in range (1,n+1):
    is_special=False
    sum_digits = 0
    num = i
    while num>0:
        sum_digits+=num%10
        num//=10
    if sum_digits==5 or sum_digits==7 or sum_digits==11:
        is_special=True
    print(f"{i} -> {is_special}")
