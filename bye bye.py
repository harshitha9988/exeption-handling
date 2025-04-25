valid=False
while not valid:
    try:
        x=int(input("enter a number:  "))

        while x%2==0:
            print("BYE")

        valid=True
    except ValueError:
        print("not valid")