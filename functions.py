def to_string(f):
    concat_strings = ""
    while 1:
        line = f.readline()
        if line == "":
            return concat_strings
        line = line.replace("\n", "")
        line = line[2:]
        concat_strings += line + ", "


def add_mail():
    return "i've added a mail (joking -_-)"

