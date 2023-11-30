# COLORS
green = '\u001b[92m'
red = '\u001b[31m'
underline = '\u001b[4m'
yellow = "\033[93m"
reset = "\033[0m"


def ask_present(f):
    presents = []
    y = 1
    while 1:
        user = input(f"Presente {y}: ")
        if user == '0':
            break
        elif user.isalpha():
            print(red, "Per favore, inserisci un numero intero", reset)
        elif user != '':
            if presents.count(int(user)) != 0:
                print(red, "Mail già aggiunta", reset)
            elif search_in_file(f, user):
                presents.append(int(user))
                print(presents)
                y += 1
            else:
                print(red, "Identificatore non trovato", reset)

    return presents


def to_string(f, presents):
    concat_strings = ""
    separator = ""
    f.seek(0)
    while 1:
        line = f.readline()
        if line == "":
            return concat_strings
        for present in presents:
            if int(line[0]) == int(present):
                line = line.replace("\n", "")
                line = line[2:]
                concat_strings += separator + line
                separator = ", "
                break


def add_mail(file):
    address_list = []

    while 1:
        mail_to_add = input(yellow + "Inserisci un indirizzo mail: " + reset)

        if mail_to_add == "":
            break
        while 1:
            f = open(file, "r")
            print(yellow + f"Inserisci il numero identificativo (id maggiore nel file: {larger_id_number(f)})" + reset, end=": ")
            f.close()
            n_address = input()

            f = open(file, "a+")
            if n_address.isalpha():
                print(red, "Per favore, inserisci un numero intero", reset)
            elif not search_in_file(f, n_address) and not search_in_list(address_list, n_address):      # if the number hasn't been used yet
                f.write(n_address + " " + mail_to_add + "\n")
                print()
                break
            else:
                print(red, "Numero già utilizzato", reset)
            f.close()


# Searches int in a file
# If 'to_search' is in the first position of the line returns True, otherwise False
def search_in_file(f, to_search):
    f.seek(0)
    while 1:
        line = f.readline()
        if line == "":
            return False
        if line[0] == to_search:
            return True


def search_in_list(list, to_search):
    for element in list:
        if element[0] == to_search:
            return True
    return False


def count_addresses(f):
    occorrences = 0
    while 1:
        line = f.readline()
        if line == "":
            return occorrences
        if line[0].isnumeric():
            occorrences += 1


def larger_id_number(f):
    larger = 0
    while 1:
        line = f.readline()
        if line == '':
            break
        if int(line[0]) > larger:
            larger = int(line[0])

    return larger


