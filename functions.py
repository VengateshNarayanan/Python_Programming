def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def multiple(a, b):
    return a * b

def div(a, b):
    # Added defensive coding or you can catch ZeroDivisionError below
    return a / b

print("------------------CALCULATOR---------------------")

try:

    a = int(input("Enter the first number: "))
    b = int(input("Enter the second number: "))

    print("Enter 1 for addition:  ")
    print("Enter 2 for subtraction: ")
    print("Enter 3 for multiplication: ")
    print("Enter 4 for division: ")

    choice = int(input("Enter the preferred number: "))

    match choice:
        case 1:
            result = add(a, b)
            print("The addition of two numbers is: ", result)

        case 2:
            result = sub(a, b)
            print("The subtraction of two numbers is: ", result)

        case 3:
            result = multiple(a, b)
            print("The multiplication of two numbers is: ", result)

        case 4:

            result = div(a, b)
            print("The division of two numbers is: ", result)

        case _:
            print("Invalid choice. Please select a number between 1 and 4.")

except ValueError:
    print("Error: Invalid entry. Please input the integer type value")

except ZeroDivisionError:
    print("Error: You can't divide any number by zero ")
