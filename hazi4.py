def szamolas():
    x = 1
    while x > 0:
        a = float(input("Enter 'a' value: "))
        b = float(input("Enter 'b' value: "))
        try:
            print(a/b)
        except ZeroDivisionError:
            print("Division by zero not allowed")
        print("Out of try except blocks")

if __name__ == "__main__":
    szamolas()