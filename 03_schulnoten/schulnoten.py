note = input('Bitte die Note eingeben: ')
note = int(note)

if note == 1:
    print('Sehr gut')
elif note == 2:
    print('Gut')
elif note == 3:
    print('Befriedigend')
elif note == 4:
    print('Genügend')
elif note == 5:
    print('Nicht genügend')
else:
    print('Ungültige Eingabe')