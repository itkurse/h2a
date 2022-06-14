# Ausgabe des kleinen 1x1
# 1 x 1 = 1
# 1 x 2 = 2
# ...
# 1 x 10 = 10 

a = 1
b = 1
while b < 11:
    ergebnis = a * b
    print(f'{a} x {b} = {ergebnis}')
    b = b + 1


a = 1
for b in range(1, 11):
    print(f'{a} x {b} = {a * b}')