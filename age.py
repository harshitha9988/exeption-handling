def is_valid_age(age_input):
    try:
        x = int(age_input)
        if 0 <= x <= 130:
            return True
        else:
            return False
    except ValueError:
        return False


y = input("Please enter your age: ")

if is_valid_age(y):
    print("Thank you! Your age is valid.")
else:
    print("Invalid age entered. Please enter a number between 0 and 130.")
