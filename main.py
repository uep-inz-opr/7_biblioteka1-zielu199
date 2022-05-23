class Ksiazka:
    def __init__(self, tytul, autor):
        self.tytul = tytul
        self.autor = autor

class Egzemplarz:
    def __init__(self, tytul, autor, rok_wydania):
        self.tytul = tytul
        self.autor = autor
        self.rok_wydania = int(rok_wydania)

def dodaj_egzemplarz_ksiazki(tytul, autor, rok_wydania):
    egzemplarz = Egzemplarz(tytul, autor, rok_wydania)
    egzemplarze.append(egzemplarz)

egzemplarze = []
ksiazki = []
iteracja = 0

liczba_ksiazek = int(input())
for ksiazka_input in range(liczba_ksiazek):
    ksiazka_input = eval(input())
    tytul = ksiazka_input[0]
    autor = ksiazka_input[1]
    rok_wydania = ksiazka_input[2]
    dodaj_egzemplarz_ksiazki(tytul, autor, rok_wydania)
    ksiazka = Ksiazka(tytul, autor)
    if iteracja == 0:
        ksiazki.append(ksiazka)
        iteracja += 1
    else:
        for book in ksiazki:
            if (ksiazka.tytul != book.tytul) and (ksiazka.autor != book.autor):
                ksiazki.append(ksiazka)
                break
            else:
                continue


for i in range(len(ksiazki)-1):
    licznik_ksiazki = 1
    for j in range(i + 1, len(ksiazki)):
        if ksiazki[i].autor == ksiazki[j].autor and ksiazki[i].tytul == ksiazki[j].tytul:
            licznik_ksiazki += 1

        else:
            continue
    ksiazki[i].licznik = licznik_ksiazki

ksiazki[len(ksiazki)-1].licznik = 1


ksiazki_bez_kopii = [None] * len(ksiazki)
for i in range(len(ksiazki)):
    ksiazki_bez_kopii[i] = ksiazki[i]


for i in range(len(ksiazki)-1):
    czy_jest_inna = False
    for j in range(i+1, len(ksiazki)):
        if ksiazki[i].autor == ksiazki[j].autor and ksiazki[i].tytul == ksiazki[j].tytul:
            if ksiazki[i].licznik > ksiazki[j].licznik:
                ksiazki_bez_kopii.remove(ksiazki[j])
        #     czy_jest_inna = True
        # else:
        #     continue


# for i in range(len(egzemplarze)):
#     print(egzemplarze[i].__dict__)
# for i in range(len(ksiazki_bez_kopii)):
#     print(ksiazki_bez_kopii[i].__dict__)

# tuple_test = f"{ksiazki_bez_kopii[0].tytul}, {ksiazki_bez_kopii[0].autor}, {ksiazki_bez_kopii[0].licznik}"
# print(tuple_test)
tuple = []

for ksiazka in ksiazki_bez_kopii:
    tupla = (ksiazka.tytul, ksiazka.autor, ksiazka.licznik)
    tuple.append(tupla)

tuple = sorted(tuple, key=lambda x: x[0])

for tupla in tuple:
    print(tupla)






