from time import sleep
from random import randint
from colorama import Fore, Style

message_to_show = input("Enter a message to show: ")

# if text contains a number convert to string
message_to_show = str(message_to_show)

base = len(message_to_show)
base += 1

while True:
    print("\033c")
    for letters in range (1, base, 2):
        y = randint(2,12)
        if letters == 1:
            print(Style.BRIGHT + Fore.RED + "{:^40}".format("\u2721"))
        elif y % 5 == 0:
            print(Fore.RED + "{:^40}".format(message_to_show[:letters]))
        elif y % 3 == 0:
            print(Fore.GREEN + "{:^40}".format(message_to_show[:letters]))
        else:
            print(Fore.MAGENTA + "{:^40}".format(message_to_show[:letters]))

    print(Fore.WHITE + "{:^39}".format("||||"))
    print(Fore.WHITE + "{:^39}".format("||||"))
    sleep(.50) 

