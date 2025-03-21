#Vyzkoušej si práci s `for` smyčkou a podmínkovým zápisem:

#1. Procházej hodnoty pro zadaný `tuple` se jménem `cisla`,
#2. .. pokud je hodnota **dělitelná třemi**, vypiš `"Fizz"`,
#3. .. pokud je hodnota **dělitelná pěti**, vypiš `"Buzz"`,
#4. .. pokud je hodnota **dělitelná třemi a současně pěti**, vypiš `"FizzBuzz"`,
#5. .. pokud nebude platit ani jedna z předchozích podmínek, vypiš hodnotu samotnou.

cisla = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15)

for cislo in cisla:
    if cislo % 3 == 0 and cislo % 5 == 0:
        print("FizzBuzz")
    elif cislo % 3 == 0:
        print("Fizz")
    elif cislo % 5 == 0:
        print("Buzz")
    else:
        print(cislo)
