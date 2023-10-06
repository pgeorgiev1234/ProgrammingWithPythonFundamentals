while True:
    line = input()
    if line=="End":
        break
    if line =="SoftUni":
        continue

    for i in line:
        print(f"{i}{i}",end="")
    print()