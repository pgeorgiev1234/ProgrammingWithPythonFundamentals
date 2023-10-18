electrons = int(input())

list_electrons = []
i = 1
while True:
    capacity = 2 * (i ** 2)
    if electrons >= capacity:
        list_electrons.append(capacity)
        electrons -= capacity
    else:
        list_electrons.append(electrons)
        electrons = 0
    if electrons == 0:
        break
    i += 1
print(list_electrons)
