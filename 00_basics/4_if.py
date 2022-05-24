'''
if Verzweigungen werden verwendet damit bestimmter Code
nur ausgeführt wird wenn eine Bedingung zutrifft (== True ist)
'''

x = 10
y = 5

'''
Bedingung ist meistens ein Vergleich
... und dazu verwendet man Vergleichsoperatoren

>   (größer als)
<   (kleiner als)
==  (Gleichheitsoperator)
!=  (Ist nicht, ungleich)
<=  (kleiner oder gleich)
>=  (größer oder gleich)

Was ist das Ergebnis eines Vergleichs? (Datentyp, Wert)?
Datentyp: boolean
boolean: True oder False
'''

# der Code der ausgeführt werden soll wenn die Bedingung 
# zutrifft muss nach dem if um einen Tab eingerückt sein
if x > y:
    print(f'{x} > {y}')
print('nach dem if')

# entweder ... oder 
if x < y:
    print(f'{x} < {y}')
else:
    print(f'{x} >= {y}')

# if ... elif ... elif ... else
if x < y:
    print(f'{x} < {y}')
elif x == y:
    print(f'{x} == {y}')
else:
    print(f'{x} > {y}')

# geschachteltes if
# ist x zwischen 2 und 10?
if x > 2:
    if x < 10:
        print('x ist eine Zahl zwischen 2 und 10')

if x > 2 and x < 10:
    print('x ist eine Zahl zwischen 2 und 10')

if x < 0 or x >= 10:
    print('Zahl ist kleiner als 0 oder größer als 9')

# wenn x nicht kleiner als 0 ist und x <= 10 ist 
if not (x < 0) and x <= 10:
    print('Zahlen von 0 bis 10 sind ok!')

if not (x == 0):
    print('x ist nicht y')