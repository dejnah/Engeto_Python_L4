#1. Procházej hodnoty pro zadaný dvoudimenzionální `list` se jménem `obsah`,
#2. .. nejprve procházej **samotné řádky**,
#3. .. následně procházej **buňku po buňce**.

obsah = [
    ['jmeno;prijmeni;email;projekt'],
    ['Matous;Holinka;m.holinka@firma.cz;hr'],
    ['Petr;Svetr;p.svetr@firma.cz;devops']
]

for radek in obsah:
      bunky = (radek[0].split(";"))
      print(bunky)
      print(len(bunky))
      for bunka in bunky:
          print(bunka, end=" | ")
      print()
      print()
