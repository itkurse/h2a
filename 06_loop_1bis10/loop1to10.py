# loop1to10.py

# while-Schleife die alle ganzen Zahlen von 1 bis 10 ausgibt 
i = 1
while i < 11:
    print(i)
    i = i + 1 

print('Jetzt mit for loop')

for i in range(1, 11):
    print(i)

# while loop von 10 bis 20 in 2er Schritten
print('while: von 10 bis 20 in 2er Schritten')

i = 10
while i <= 20:
    print(i)
    i = i + 2

print('for: von 10 bis 20 in 2er Schritten')
for i in range(10, 21, 2):
    print(i)