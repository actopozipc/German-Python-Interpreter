importiere numpy als np
von numpy importiere wurzel
Klasse Person:
    def __init__(selbst, name, alter):
        selbst.name = name
        selbst.alter = alter
    
    def gruesse(selbst):
        drucke(f'Hallo, ich bin {selbst.name} und {selbst.alter} Jahre alt.')

p = Person('Max', 25)
p.gruesse()

zahl = 10
solange zahl > 0:
    wenn zahl % 2 == 0:
        drucke(f'{zahl} ist gerade.')
    sonst:
        drucke(f'{zahl} ist ungerade.')
    zahl -= 1

liste = [1, 2, 3, 4, 5, 7, 8]
für element in liste:
    wenn element == 1:
        fortsetze
    andernfalls element == 7:
        breche
    drucke(f'Die Wurzel von {element} ist {np.wurzel(element)}.')
    
versuche:
    1 / 0
Ausnahme NullteilungsFehler als e:
    drucke(f'Division durch Null: {e}.')
schlussendlich:
    drucke('Das Programm ist fertig')
