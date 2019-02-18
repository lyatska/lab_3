import json

def research():
    """
    Search needed key's value in "twittie.json".
    """

    info = json.load(open("twittie.json", "r", encoding = "utf-8"))
    print(info)
    search = input("What key's value do you want to see? ")
    section = info[0][search]
    print(section)

    s = input("Please, enter the name of the next key:")
    if s not in section:
        print("Sorry,there is no such a key")
    else:

        print(section[s])
        m = input("Print the next key if needed:")
        if m not in section[s]:
            print("Sorry,there is no such a key")
        else:
            print(section[s][m])


print(research())
