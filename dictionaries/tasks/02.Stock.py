input1=input().split()
inventory={}

for i in range(0,len(input1),2):
    key = input1[i]
    value = input1[i+1]
    inventory[key]=int(value)

input2=input().split()

for x in input2:
    if x in inventory:
        print(f"We have {inventory[x]} of {x} left")
    else:
        print(f"Sorry, we don't have {x}")