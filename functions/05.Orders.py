def orders(order,ammount):
    if order=="coffee":
        return 1.50*ammount
    elif order == "coke":
        return  1.40*ammount
    elif order == "water":
        return 1.00*ammount
    elif order=="snacks":
        return 2.00*ammount

product = input()
ammount = int(input())


print(f"{orders(product,ammount):.2f}")
