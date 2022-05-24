# Für die übergebene Jahreszahl year wird überprüft ob es sich
# um ein Schaltjahr handelt oder nicht (True oder False)
# Function gibt True zurück wenn es ein Schaltjahr ist
# Function gibt False zurück wenn es kein Schaltkahr ist
def is_leap_year(year):
    if year % 4 == 0 and year % 100 != 0:
        return True
    if year % 100 == 0 and year % 400 != 0:
        return False 
    if year % 400 == 0:
        return True 
    return False 

while True:
    year = int(input('Bitte eine Jahreszahl eingeben: '))
    if is_leap_year(year):
        print(f'{year} ist ein Schaltjahr!')
    else:
        print(f'{year} ist kein Schaltjahr!')



