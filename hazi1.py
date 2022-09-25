def kifejezes(name):
    name = str(name.lower())

    dict = {}
    for i in name:
        keys = dict.keys()
        if i in keys:
            dict[i] += 1
        else:
            dict[i] = 1
    print(dict)

    print("Fordítva: ", name[-1::-1])

    list = (name.split(" "))
    print("Listába rendezve szavanként: ", list)


if __name__ == "__main__":
    mondat = input("Adjon meg egy mondatot: ")
    kifejezes(mondat)
