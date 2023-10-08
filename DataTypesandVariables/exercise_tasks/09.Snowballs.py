n = int(input())

text = ""
highest_value = 0
for i in range(n):
    weight=int(input())
    time=int(input())
    quality=int(input())
    value = (weight / time) ** quality
    if value>highest_value:
        highest_value=value
        text=f"{weight} : {time} = {highest_value:.0f} ({quality})"

print(text)