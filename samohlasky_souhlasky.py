#program, který spočítá kolik samohlásek a souhlásek obsahuje zadaný string:'
#Jednotlivé kroky, které program musí obsahovat:
#1.	Vytvoř proměnnou veta, typu str, která obsahuje hodnotu: "Zvuk řeči je produkován poměrně otevřenou konfigurací vokálního traktu",
#2.	proměnnou samohlasky, typu str, která obsahuje 'aeiouáéíóú',
#3.	proměnnou souhlasky, typu str, která obsahuje 'bcčdďfghjklmnňprřsštťvzžcdž',
#4.	proměnnou vysledek, typu dict, který obsahuje klíče "souhlasky" a "samohlasky". Slovník bude evidovat výskyty těchto hodnot,
#5.	iteraci přes všechny znaky v proměnné veta,
#6.	pokud znak není ani samohláska, ani souhláska, tak jej přeskoč,
#7.	pokud je znak samohláska nebo souhláska, inkrementuj ve slovníku vysledek správný klíč,
#8.	nakonec vypiš konečný stav podle ukázky níže. Počet souhlásek: 35 | Počet samohlásek: 25

veta = "Zvuk řeči je produkován poměrně otevřenou konfigurací vokálního traktu"
samohlasky = "aeiouáéíóú"
souhlasky = "bcčdďfghjklmnňprřsštťvzžcdž"
# Slovník s evidencí výskytu jednotlivých typů písmen
vysledek = {"samohlasky": 0, "souhlasky": 0}

#smyčka
for znak in veta:
    #pokud je znak samohláska
    if znak.lower() in samohlasky:
        vysledek["samohlasky"] = vysledek["samohlasky"] + 1
    #pokud je znak souhláska
    elif znak.lower() in souhlasky:
        vysledek["souhlasky"] = vysledek["souhlasky"] + 1

print("počet souhlásek:", vysledek["souhlasky"], " | počet samohlásek:", vysledek["samohlasky"])
