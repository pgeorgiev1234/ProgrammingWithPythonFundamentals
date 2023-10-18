version = [int(x) for x in input().split(".")]

if version[-1] < 9:
    version[-1] += 1
elif version[-1] == 9 and version[1] == 9:
    version[-1] = 0
    version[1] = 0
    version[0] += 1
elif version[-1] == 9:
    version[-1] = 0
    version[1] += 1

print(f"{version[0]}.{version[1]}.{version[2]}")
