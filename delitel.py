#Dělitel
#V této úloze vytvoř program, který potřebuje od uživatele start, stop a delitel. Po zapracování vypíše všechna celá čísla v intervalu od start, do stop, která jsou  dělitelná hodnotou v delitel.
#Jednotlivé kroky, které program musí obsahovat:
#1.	Zapiš hodnoty do proměnné uvedené výš.
#2.	ověří jestli jsou proměnné start, stop a delitel datový typ int (pomocí built-in funkce isinstance),
#3.	pokud jsou int, vypiš oznámení dle ukázky níž,
#4.	pokud alespoň jeden není int, vypiš oznámení dle ukázky níž a ukonči skript,
#5.	jestli jsou jednotlivé hodnoty z intervalu dělitelné hodnotou v proměnné delitel, potom je přidej do zadaného seznamu vysledek,
#6.	po skončení iterace všech hodnot vypiš výsledné hodnoty podle vzoru níže.

#zadaná proměnná
vysledek = list()

# Zadané hodnoty:
start = 3
stop = 9
delitel = 3

hodnoty = list(range(start, stop + 1))

#print(hodnoty)
#print(type(start))
#print(type(stop))
#print(type(delitel))
#print(f"Zadaný rozsah <{hodnoty[0]}, {hodnoty[-1]}>")

#for cislo in hodnoty:
#    if cislo % 3 == 0:
#        vysledek.append(cislo)
#        # Start: 3, Stop: 9, Dělitel: 3
#print(f"Čísla dělitelná {delitel}: {vysledek}")

if isinstance(start, int) and isinstance(stop, int) and isinstance(delitel, int):
    print(f"Zadaný rozsah: <{start}, {stop}>")

    # Iteruj zadanými čísly
    for cislo in hodnoty:
        #pokud je cislo delitelne promennou "delitel"
        if cislo % delitel == 0:
            #přidám ho do promměnné "výsledek"
            vysledek.append(cislo)
    print(f"Čísla dělitelná {delitel}: {vysledek}") 
else:
    print("Zadané vstupy musí mýt čísla.")  
