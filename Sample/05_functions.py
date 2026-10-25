class calculate:
    def add(self , a , b):
        return a+b

    def sub(self , a , b):
        return a-b

    def mul(self , a , b):
        return a*b

    def div(self , a , b):
        try:
            return a/b
        except ZeroDivisionError:
            return "Cannot divide by zero"


calc = calculate()

print("Enter 1 for addition:")
print("Enter 2 for subtraction")
print("Enter 3 for multiplication")
print("Enter 4 for division")

choice = input("Enter your choice: ")

