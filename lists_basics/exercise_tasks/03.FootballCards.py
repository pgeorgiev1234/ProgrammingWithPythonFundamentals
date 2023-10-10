tekst = input().split()

first_sent_off=0
second_sent_off=0

first_players=[]
second_players=[]

should_terminate=False

for card in tekst:
    if card in first_players or card in second_players:
        continue
    txt=card.split("-")
    team=txt[0]
    player=txt[1]

    if team=="A":
        first_sent_off+=1
        first_players.append(card)
    else:
        second_sent_off+=1
        second_players.append(card)
    if first_sent_off>4 or second_sent_off>4:
        should_terminate=True
        break

print(f"Team A - {11-first_sent_off}; Team B - {11-second_sent_off}")
if should_terminate:
    print("Game was terminated")