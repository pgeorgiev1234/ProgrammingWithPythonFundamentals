year = int(input())

while True:
    year+=1
    happy_year = set(str(year))
    if len(happy_year)==4:
        print(year)
        break