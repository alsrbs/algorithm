card = {
    'P': {'01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13'},
    'K': {'01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13'},
    'H': {'01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13'},
    'T': {'01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13'},
}
lost_card = input()
t = True
for i in range(0,len(lost_card),3):
    if lost_card[i+1:i+3] in card[lost_card[i]]:card[lost_card[i]].discard(lost_card[i+1:i+3])
    else:t = False;break
if t:print(f'{len(card["P"])} {len(card["K"])} {len(card["H"])} {len(card["T"])}')
else:print('GRESKA')

