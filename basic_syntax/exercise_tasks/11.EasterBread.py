budget = float(input())
price_flour = float(input())
price_eggs = 0.75*price_flour
price_milk = 1.25*price_flour/4

price_loaf = price_milk+price_flour+price_eggs
eggs = 0
loaves = 0
while budget>=price_loaf:
    budget-=price_loaf
    loaves+=1
    eggs +=3
    if loaves%3==0:
        eggs -=(loaves-2)

print(f"You made {loaves} loaves of Easter bread! Now you have {eggs} eggs and {budget:.2f}BGN left.")
