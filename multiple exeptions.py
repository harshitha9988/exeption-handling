try:
    x,y=eval(input("enter 2 number, with a comma seperating them  "))
    z=x/y
    print("total: ",z)

except ZeroDivisionError:
    print("you can't divide by 0!")

except SyntaxError:
    print("There is no comma. Please seperate the numbers with a comma")

except:
    print("the input is incorrect")

else:
    print("no exceptions")

finally:
    print("this will execute no matter what")