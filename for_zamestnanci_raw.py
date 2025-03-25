# Domácí úkol - skripta 4 Val
# práce s `for` smyčkou:

# výše zadaných jmen vytvoř slovník, kde budou klíče celá jména a hodnoty budou nestované slovníky, obsahující:
# klíče křestní jméno, příjmení a email. Viz. ukázka:


#{'Adéla Kavková': {'email': 'a.kavková@firma.cz',
#                   'krestni_jmeno': 'Adéla',
#                   'prijmeni': 'Kavková'},
# 'Alena Kubiková': {'email': 'a.kubiková@firma.cz',
#                    'krestni_jmeno': 'Alena',
#                    'prijmeni': 'Kubiková'},
# 'Aleš Svoboda': {'email': 'a.svoboda@firma.cz',
#                  'krestni_jmeno': 'Aleš',
#                  'prijmeni': 'Svoboda'},


zamestnanci_raw = """
Helena Vybíralová
Wendy Štrumlová
Marie Vybíralová
Stanislav Bechyňka
Zdeňka Urbánková
Lukáš Riečan
Veronika Koudelová
Františka Vorlová
Ilie Seleš
Martin Železný
Petra Niklesová
Bohumil Skok
Jakub Šmíd
Jarmila Procházková
Dagmar Hlavatá
Jiří Nguyen Thanh
Marie Franková
Dana Ulrichová
Jana Hranická
Hana Budošová
Ivan Široký
Květoslava Jiráčková
Pavel Przywara
Josef Umlauf
Tomáš Granzer
Miroslav Kuba
Miloslava Adámková
Marie Karlíková
Jaroslav Hronský
Vlasta Karlíková
Andrea Žatková
Zuzana Lokočová
Ondřej Ptáček
Zdeněk Najman
Tereza Šebešová
Antonie Skokánková
Jan Lion
Václav Vecko
František Vajgl
Adéla Kavková
Amália Vacková
Anna Pažická
Ivo Pustějovský
Antonín Pavela
Jitka Adamová
Libuše Hamroziová
Drahomíra Balzerová
Marek Suchánek
Petr Vavrinec
Jonáš Stuchlý
Jaromír Pecen
Markéta Kyliánková
Marina Pečenková
Ivana Perdochová
Michaela Drápalová
Michael Mentlík
Rudolf Špičák
Žaneta Holá
Blanka Lišková
Eva Svatoňová
Rostislav Hoang
Martina Kalivodová
Milan Hruška
Zdenka Marková
Lenka Schambergerová
Růžena Martinů
Věra Řezanková
Marie Pečenková
Miloš Váchal
Jaroslava Hrubá
Petr Pecen
Pavla Konvicová
Lucie Marešová
Květuše Zdráhalová
Vlastimila Svatošová
Zora Michalčíková
Daniel Švejnoha
Klára Brunclíková
Vladimír Bauer
Michal Slaný
Jiřina Novosadová
Karel Sršeň
Stanislava Lakosilová
Filip Černý
Alena Kubiková
Sára Kotrlová
Alois Rejlek
Božena Novotná
Maryana Nováková
Kateřina Máslová
Ladislav Dvořák
Radek Varga
Petr Dvořák
Ludmila Jaklová
Renáta Foubíková
Nikola Lehká
Dominika Riegerová
Patrik Polák
Soňa Štrbová
David Matoušek
Liubov Hollíková
Monika Poláková
Marie Jaklová
Aleš Svoboda
Roman Kolínský
Karolína Košiková
"""



import pprint
zamestnanci = {}

for cele_jmeno in zamestnanci_raw.split("\n"):
    if cele_jmeno: 
        krestni, prijmeni = cele_jmeno.split(" ", 1) #předpokládám, že pokud je ve jméně více mezer, bude to více příjmení
        email = krestni[0].lower() + "." + prijmeni.lower().replace(" ", ".") + "@firma.cz"
        zamestnanci[cele_jmeno] = {"email": email,
                                     "krestni_jmeno": krestni,
                                     "prijmeni": prijmeni}
pprint.pprint(zamestnanci)
