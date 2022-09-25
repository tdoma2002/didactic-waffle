meret = float(input("Adjon meg egy számot és egy mértékegységet (cm/inch):\n"))
egyseg = input()

if egyseg == "inch":
    cm = 2.54
    print(cm * meret, "cm")

elif egyseg == "cm":
    inch = 0.393700787
    print(inch * meret, " inches")

else:
    print("A mértékegység nem megfelelő!")
