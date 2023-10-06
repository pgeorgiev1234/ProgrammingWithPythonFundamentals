counter=0
while True:
    event = input()
    if event=="END":
        break
    if event == "dog" or event=="cat" or event=="coding" or event=="movie":
        counter+=1
    if event == "DOG" or event == "CAT" or event == "CODING" or event == "MOVIE":
        counter+=2
if counter>5:
    print("You need extra sleep")
else:
    print(counter)