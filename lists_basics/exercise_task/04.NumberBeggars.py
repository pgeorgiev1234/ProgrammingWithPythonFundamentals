listi = input().split(", ")
beggars=int(input())

beggars_money=[0]*beggars

for idx in range(len(listi)):
    beggar_index=idx%beggars
    num = int(listi[idx])
    beggars_money[beggar_index]+=num

print(beggars_money)
