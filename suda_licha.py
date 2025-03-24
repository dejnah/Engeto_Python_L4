#Sudá vs. Lichá

#V této úloze vytvoř program, který sečte odděleně všechna sudá a všechna lichá čísla ze seznamu.
#Na konci by měl program vypsat absolutní hodnotu rozdílu mezi těmito součty.
#Tvým ukolem je zjistit, jak iterovat každým prvkem v seznamu čísel, ne psát součet manuálně.
#Jednotlivé kroky, které program musí obsahovat:
#1.	Zapiš hodnoty do proměnné uvedené výš.
#2.	sečti všechna sudá čísla a výsledek ulož do proměnné suda,
#3.	sečti všechna lichá čísla a výsledek ulož do proměnné licha,
#4.	nakonec získáš rozdíl mezi těmito dvěma součty (proměnná vysledek),
#5.	zajisti, že výsledek nebude záporné číslo (k tomu by ti mohly pomoci built-in funkce pro numerické typy, zmiňované v první lekci). Rozdíl je: ?

cisla = [1, 2, 3, 4, 5, 6, 7, 8]

suda_cisla = []
licha_cisla = []

for cislo in cisla:
    if cislo % 2 == 0:
        suda_cisla.append(cislo)
    else:
        licha_cisla.append(cislo)

print(suda_cisla)
print(licha_cisla)
print()

suda = (sum(suda_cisla))
licha =(sum(licha_cisla))
print(suda)
print(licha)
print()

celkem = abs(suda - licha)
print(celkem)
print("Rozdíl je:", celkem)

#jiné řešení:
print()
print("Jiné řešení")
cisla_2 = [1, 2, 3, 4, 5, 6, 7, 8]

licha_2 = 0
suda_2 = 0

for num in cisla_2:
    if num % 2 == 0:
        suda_2 = suda_2 + num
    else:
        licha_2 = licha_2 + num

#print(suda_2)
#print(licha_2)
vystup = abs(suda_2 - licha_2)
print('Rozdíl je:', vystup)
