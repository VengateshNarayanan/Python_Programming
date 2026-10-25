file = open("hello.txt" , "r")
print(file.readline())
print(file.readline())

print(file.readline())
print(file.readline())
print(file.readline())

file.close()

file2 = open("data.txt" , "w")
file2.write(input("Enter the text to be inserted inside the file data.txt "))
#print(file2.write())
file2.close()

file2 = open("data.txt" , "a")
file2.write("\nwelcome all")
file2.close()

with open("data.txt" , "r") as file:
    print(file.read())

with open("data.txt") as file:
    print(file.read(5))

print("Enter 1 for inputing your details into student details: ")
print("Enter 2 for displaying the student already present in the record: ")
print("Enter 3 to exit....")

choice = int(input("Enter the choice you want: "))

match choice:
    case 1:
        with open("student.txt" , "a") as file:
            file.write(input("Enter the name:\n ")+ " | ")
            file.write(input("Enter the roll no:\n ")+ " | ")
            file.write(input("Enter the marks:\n ")+ "\n")

    case 2:
        with open("student.txt" , "r") as file:
            print(file.read())


    case 3:
        print("Exiting.....")

    case _:
        print("Invalid Input Please try again......")

    

