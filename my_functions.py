from os import listdir, getcwd, mkdir, path, chdir
from random import randint
from shutil import rmtree
# --------------------------------------------
def kto_jest():
    cwd = getcwd()
    files = listdir(cwd)   
    kto = []
    for i in files:
        if path.isdir(i) and i != '__pycache__':
            kto.append(i)
    return kto
# --------------------------------------------
def podaj_dane():
    inp = input('Podaj osobe \t')
    if path.exists(inp):
        chdir(inp)
        files = listdir(getcwd())
        for i in files:
            with open(i,'r') as myfile:
                print(f'{i} \t{myfile.read()}')
        chdir('..')
    else:
        print('Taka osoba nie istnieje')
# --------------------------------------------
def dodaj_osobe():
    inp = input('Podaj osobe \t')
    if path.exists(inp):
        print('Taka osoba istnieje ')
    else: 
        mkdir(inp)
        print(f'Dodano {inp}')
# --------------------------------------------
def dodaj_przedmiot():
    inp = input("Podaj osobe \t")
    if path.exists(inp):
        chdir(inp)
        inp = input('Podaj przedmiot \t')
        lista = listdir()
        if inp+'.txt' in lista:
            print('Taki przedmiot już istnieje')
            chdir('..')
        else:
            print(f'Dodano plik {inp}.txt')
            with open(f'{inp}.txt', 'w') as myfile:
                myfile.write('')
            chdir('..')
    else:
        print('Podana osoba nie istnieje')
# --------------------------------------------
def policz_srednie(data):
    suma = 0
    li = 0
    for i in data:
        li += 1
        if i == '1' or i == '2' or i == '3' or i == '4' or i == '5' or i == '6':
            suma += int(i)
    return suma/li

def generuj_raport():
    inp = input('Popdaj osobe \t')
    if path.exists(inp):
        chdir(inp)
        lista = listdir()
        raport = ''
        for i in lista:
            with open(i, 'r') as myFile:
                data = myFile.read()
                raport += f'{i} \t {data} \t srednia {policz_srednie(data)}'
            raport  += '\n'
        chdir('..')
        with open(f'raport_{inp}.txt', 'a') as myFile:
            myFile.write(raport)
        print(f'wygenerowano \t raport_{inp}.txt ')
    else:
        print('Taka osoba nie istnieje')
# --------------------------------------------
def dodaj_ocene():
    inp = input('opdaj osobe \t')
    if path.exists(inp):
        chdir(inp)
        lista = listdir()
        print(lista)
        inp = input('Podaj przedmiot \t') + '.txt'
        if inp in lista:
            inp_2 = input('Podaj ocene \t') + ' '
            with open(inp, 'a+') as myFile:
                print('-'*30)
                myFile.write(f' {inp_2}')
                myFile.seek(0)
                data = myFile.read()
                print(f'{data} \t ocena dodana {inp_2}')
                print('-'*30)
        else:
            print('Nie ma takiego przedmiotu')
        chdir('..')
    else:
        print('Nie ma takiej osoby')
# --------------------------------------------
def usun_osobe():
    inp = input('Podj plik który chcesz usunac \t')
    if path.exists(inp):
        x = randint(100,1000)
        inp_2 = int(input(f'podaj {x} aby potwierdzić \t'))
        if inp_2 == x:
            rmtree(inp)
            print('Plik usuniety')
        else:
            print('Zła liczba operacja cofnieta')
    else:
        print('Nie ma takiej osoby')
# --------------------------------------------
def dodaj_sprawdzian():
    inp = input("Podaj nazwe kalendarza \t")
    if path.exists(inp):
        chdir(inp)
        inp = input('Podaj date i nazwe \t')
        lista = listdir()
        if inp+'.txt' in lista:
            print('')
            chdir('..')
        else:
            print(f'Dodano sprawdzian/kartkówkę {inp}.txt')
            with open(f'{inp}.txt', 'w') as myfile:
                myfile.write('')
            chdir('..')
    else:
        print('Podana osoba nie istnieje')
#----------------------------------------------
def stwórz_kalendarz():
    inp = input('Podaj nazwe kalendarza \t')
    if path.exists(inp):
        print('Taki kalendarz nie istnieje ')
    else: 
        mkdir(inp)
        print(f'Dodano {inp}')
#--------------------------------------------------
def wyświetl_kalendarz():
    inp = input('Podaj nazwe kalendarza \t')
    if path.exists(inp):
        chdir(inp)
        files = listdir(getcwd())
        for i in files:
            with open(i,'r') as myfile:
                print(f'{i} \t{myfile.read()}')
        chdir('..')
    else:
        print('Taki kalendarz nie istnieje')