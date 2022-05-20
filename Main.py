from os import getcwd
from my_functions import podaj_dane, wyświetl_kalendarz, kto_jest, dodaj_osobe, dodaj_przedmiot, dodaj_sprawdzian, generuj_raport, dodaj_ocene, stwórz_kalendarz, usun_osobe

def main():
    while True:
        # -------------------------------------------------------
        print('-'*50)
        print(getcwd())
        print(kto_jest())
        print('A - Wyswietl dane osoby')
        print('B - Dodaj osobe')
        print('C - Dodaj przemiot')
        print('E - Dodaj kalendarz')
        print('G - Dodaj sprawdzian/kartkówkę')
        print('T - wyświetl kalendarz')
        print('R - Generuj Raport')
        print('D - Dodaj ocene')
        print('U - Usun osobe')
        print('X - Wyjdź z programu')
        print('Z - dodaj sprawdzian')
        print('-'*50)
        # -------------------------------------------------------
        inp = input('?  \t')
        if inp.upper() == 'A':
            podaj_dane()
        # -------------------------------------------------------
        elif inp.upper() == 'B':
            dodaj_osobe()
        #--------------------------------------------------------
        elif inp.upper() == 'T':
            wyświetl_kalendarz()
        # -------------------------------------------------------
        elif inp.upper() == 'C':
            dodaj_przedmiot()
        # -------------------------------------------------------
        elif inp.upper() == 'E':
            stwórz_kalendarz()
        #--------------------------------------------------------
        elif inp.upper() == 'G':
            dodaj_sprawdzian()
        #--------------------------------------------------------
        elif inp.upper() == 'R':
            generuj_raport()
        # -------------------------------------------------------
        elif inp.upper() == 'D':
            dodaj_ocene()
        # -------------------------------------------------------
        elif inp.upper() == 'U':
            usun_osobe()
        # -------------------------------------------------------        
        elif inp.upper() == 'Z':
            dodaj_sprawdzian()
        #--------------------------------------------------------
        elif inp.upper() == 'X':
            print('Program zakończył działanie')
            break
        # -------------------------------------------------------
        else:
            print('Nie ma takiej komendy')
        inp = input('kliknij ENTER aby wrócić do głównego menu')

#----------------------------------------------------------------

if __name__ == '__main__':
    main()