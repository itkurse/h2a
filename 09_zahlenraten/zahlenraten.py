'''
Definiere das Minumum in der Variable min
Definiere das Maximum in der Variable max 
Ermittle eine Zufallszahl zwischen min und max und speichere sie in random_number 
Erstelle die int-Variable counter mit dem Startwert 0
Wiederhole solange guess nicht gleich random_number ist:
    frage den User nach einer Zahl und speichere sie in guess 
    wenn guess < random_number dann ausgeben "Die gesuchte Zahl ist größer"
    wenn guess > random_number dann ausgeben "Die gesuchte Zahl ist kleiner"
    erhöhe den Counter um 1
Gebe aus "Zahl richtig erraten! Du hast {counter} Versuche benötigt!"
'''
from random import randint 

min = 1 
max = 10 
random_number = randint(min, max)
counter = 0
guess = 0 
while guess != random_number:
    guess = int(input(f'Rate eine Zahl zwischen {min} und {max}: '))
    if guess < random_number:
        print('Die gesuchte Zahl ist größer!')
    if guess > random_number:
        print('Die gesuchte Zahl ist kleiner!')
    counter = counter + 1
print(f'Zahl richtig erraten! Du hast {counter} Versuche benötigt!')