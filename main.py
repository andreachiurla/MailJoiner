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
    # print commands list
    print(green + "--- COMANDI ---", reset)
    print("-Esci dal programma ", yellow + "[0]", reset)
    print("-Richiedi stringa mail dei presenti ", yellow,  "[1]", reset)
    print("-Aggiungi mail ", yellow, "[2]", reset)
    print("-Elimina tutte le mail ", yellow, "[404]", reset)
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
            if concat_strings != "":
                print(yellow, "Incolla:", reset, f"\n{concat_strings}")
        case '2':
            f = open(file, "a+")
            print(add_mail(f))
            f.close()
        case '404':
            user = input(yellow + "Digita 'si' per confermare il reset del file: " + reset)
            if user.lower() == 'si':
                f = open(file, "w")
                print(red, "Reset eseguito con successo", reset)
                f.close()
            else:
                print(red, "Reset non eseguito", reset)

        case _:
            print(red, "Input inserito non valido", reset)

    print("\n")
