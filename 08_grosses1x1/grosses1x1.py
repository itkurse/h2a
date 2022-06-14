'''
1 x 1 = 1
2 x 1 = 2 
3 x 1 = 2 
4 x 1 = 2 
5 x 1 = 2 
6 x 1 = 2 
7 x 1 = 2 
8 x 1 = 2 
9 x 1 = 2 
10 x 1 = 10
1 x 2 = 2
2 x 2 = 4
3 x 2 = 4
4 x 2 = 4
5 x 2 = 4
...
10 x 2 = 20

...
10 x 10 = 100 
'''

print('Lösung mit for')
for a in range(1, 11):
    for b in range(1, 11):
        ergebnis = a * b
        print(f'{a} x {b} = {ergebnis}')

print('Lösung mit while:')
a = 1
while a < 11:
    b = 1
    while b < 11:
        ergebnis = a * b
        print(f'{a} x {b} = {ergebnis}')
        b = b + 1
    a = a + 1