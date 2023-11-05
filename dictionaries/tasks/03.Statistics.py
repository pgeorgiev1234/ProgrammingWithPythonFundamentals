products={}

command = input().split(": ")
while command[0]!="statistics":
    product = command[0]
    quantity = command[1]
    if product not in products:
        products[product]=0
    products[product]+=int(quantity)
    command=input().split(": ")

print("Products in stock:")
for (product,quantity) in products.items():
    print(f"- {product}: {quantity}")
print(f"Total Products: {len(products.keys())}")
print(f"Total Quantity: {sum(products.values())}")