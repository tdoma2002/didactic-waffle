def haromszog():
    a = input("a: ")
    b = input("b: ")
    c = input("c: ")
    if a + b > c:
        if a + c > b:
            if b + c > a:
                print("Megszerkeszthető")
    else:
        print("Nem megszerkeszthető")

if __name__=="__main__":
    haromszog()
