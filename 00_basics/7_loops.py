'''
Schleifen werden verwendet ... 
- Ich möchte (Code) wiederholen solange eine Bedingung erfüllt ist
- um über Sequenzen (Listen, Tuple, Dictionaries, Strings, Sets)
  zu iterieren
'''

people = ['Marc', 'Celina', 'Luki', 'Maurice']

# iterieren über eine Liste
for person in people:
    print(f'Aktuelle Person ist {person}')


# break: höre mit der Schleife (und fahre nach der Schleife fort)
# --> beendet die Schleife
for person in people:
    # wenn person Luki, höre mit der Schleife auf
    if person == 'Luki':
        break 
    print(f'Die Person ist {person}')


# continue: bricht nur den aktuellen Schleifendurchgang ab,
# macht mit dem nächsten Schleifendurchgang weiter
# wir wollen Luki nur überspringen
for person in people:
    if person == 'Luki':
        continue
    print(f'Nicht übersprungen wurde {person}')


# über Index auf jedes Element des Arrays zugreifen
for i in range(len(people)):
    print('i=', i, people[i])


# Zahlen von 5 bis 10
for i in range(5, 11):
    print('5-10: ', i)

# C, C++, C#, Java, PHP, ... 
# for(int i = 5; i < 11; i++){}

# Auf jedes Zeichen in einem String zugreifen
for zeichen in "Viel Erfolg!":
    print(zeichen)


'''
Bei der for-Schleife weiß ich am Anfang der Schleife wie oft ich
den Schleifenkörper durchführen möchte. 

Bei der while-Schleife weiß ich zu Beginn der Schleife noch nicht
wie oft der Schleifenkörper ausgeführt wird. 
'''

from random import randint 
# wiederhole solange bis random die Zahl 5 erraten hat
keepGoing = True
while keepGoing == True:
    guess = randint(1, 10)
    if guess == 5:
        print('Computer hat 5 erraten!')
        keepGoing = False 
    else:
        print(f'Computer hat {guess} gerate')
