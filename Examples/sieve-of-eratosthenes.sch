def ist_primzahl(zahl):
    wenn zahl < 2:
        Rückkehr Falsch
    für teiler in reichweite(2, int(zahl ** 0.5) + 1):
        wenn zahl % teiler == 0:
            Rückkehr Falsch
    Rückkehr Wahr
# upper bound
obere_grenze = int(eingabe("Gib die obere Grenze ein: "))

# list of prime numbers
primzahlen = []

# search for primes
für zahl in reichweite(2, obere_grenze + 1):
    wenn ist_primzahl(zahl):
        primzahlen.append(zahl)

# output
drucke("Primzahlen von 2 bis", obere_grenze, ":")
für i,primzahl in enumeriere(primzahlen):
    drucke(f"Die {i}. Primzahl ist ",primzahl)