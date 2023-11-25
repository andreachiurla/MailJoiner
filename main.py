from functions import *

# COLORS
green = '\u001b[92m'
red = '\u001b[31m'
underline = '\u001b[4m'
yellow = "\033[93m"
reset = "\033[0m"

file = "AddressList.txt"

# file creation
f = open(file, "a")
f.close()

while 1:
    print(green + "--- COMANDI ---", reset)
    print("-Esci dal programma ", yellow + "[0]", reset)
    print("-Richiedi stringa mail dei presenti ", yellow,  "[1]", reset)
    print("-Aggiungi mail ", yellow, "[2]" + reset)
    print("")

    userRequest = input(yellow + "Inserisci comando: " + reset)

    match userRequest:
        case '0':
            print(red, "Chiudo il programma...\n", reset)
            break
        case '1':
            f = open(file, "r")
            presents = ask_present(f)
            concat_strings = to_string(f, presents)
            f.close()
            print(yellow, "Incolla:", reset, f"\n{concat_strings}")
        case '2':
            f = open(file, "a+")
            print(add_mail(f))
            f.close()
        case _:
            print(red, "Input inserito non valido", reset)

    print("\n")
