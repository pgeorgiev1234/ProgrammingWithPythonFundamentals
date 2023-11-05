words = input().lower().split()
rechnik = {}

for word in words:
    if word not in rechnik:
        rechnik[word]=0
    rechnik[word]+=1

for key,value in rechnik.items():
    if value%2==1:
        print(key, end=" ")