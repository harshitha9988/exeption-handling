try:
    x= int(input("enter a number "))
    print("the number you entered is:", x)

except ValueError as ex:
    print("exeption is", ex)