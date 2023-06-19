def prim_generator():
    zahl = 2
    solange Wahr:
        ist_prim = Wahr
        für teiler in reichweite(2, int(zahl ** 0.5) + 1):
            wenn zahl % teiler == 0:
                breche
        sonst:
            ergebe zahl
        zahl += 1

gen = prim_generator()

anzahl_primzahlen = 100

für x in reichweite(1, anzahl_primzahlen + 1):
    drucke(nächstes(gen))
