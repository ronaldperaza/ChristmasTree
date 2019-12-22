from time import sleep
from random import randint
from colorama import Fore, Style

# COLORES DISPONIBLES PARA Fore
# BLACK, RED GREEN YELLOW, BLUE,
# MAGENTA, CYAN WHITHE

texto1=input("Ingresa un Mensaje de Navidad: ")
#texto1=str(texto1)
base1=len(texto1)
base1+=1

while True:
    print('\033c')  #para limpiar la consola
    for x in range (1,base1,2):
        y=randint(2,12)
        if x==1:
            # .format("\u2721") contiene la estrella
            print(Style.BRIGHT+Fore.RED+"{:^40}".format("\u2721"))  #BRIGHT
        elif y%5==0:
            print(Fore.RED+"{:^40}".format(texto1[:x]))
        elif y%3==0:
            print(Fore.GREEN+"{:^40}".format(texto1[:x]))
        else:
            print(Fore.MAGENTA+"{:^40}".format(texto1[:x]))

    print(Fore.WHITE+"{:^39}".format("||||"))
    print(Fore.WHITE+"{:^39}".format("||||"))
    sleep(.50)

