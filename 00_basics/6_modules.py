'''
Ein Modul ist im Grunde genommen eine Datei die eine Reihe von Funktionen enthält.
Diese Datei kann mit einem "import" zu unseren Anwendungen hinzugefügt werden. 

Es gibt
- Core Python Module (sind schon dabei), z. B. random, datetime, ... 
- Module die über den pip Package Manager installiert werden können, z. B. Django, 
  matplotlib
- Custom Modules (selbst geschriebenen Module)
'''

# import core python module
# importiere das gesamte modul ramdom 
import random 

# zufallszahl erzeugen
# wenn das gesamte Modul importiert wurde, können die darin enthaltenen
# Funktionen nur mit modulname.funktionsname() aufgerufen werden
zufall = random.randint(5, 100)
print('Zufallszahl', zufall)
print('Zufalls-Kommazahl:', random.uniform(1, 10))

'''
Alternative: Nur bestimmte Funktionen aus einem Modul importieren:
from modulname import funktionsname
'''
from random import randrange
print('Randrange wurde direkt importiert', randrange(5))



# importiere das core python modul datetime
import datetime # importiere das gesamte Modul datetime
# ODER nur einen Teil daraus
from datetime import date 


'''
pip modules (package manager)

Ein Modul über den pip package manager installieren:
pip install <modulname>
pip install camelcase 

Welche Module habe ich schon installiert?
pip freeze
'''

from camelcase import CamelCase

cc = CamelCase()
print(cc.hump('hallo welt mir gehts gut'))


'''
Eigenes Modul "validator"
dazu: im gleichen Ordner eine Datei anlegen, und der Dateiname ist der Modulname
'''
import validator 
print('check email', validator.validate_email('a@b.com'))
print('check passwort', validator.validate_password('abc'))