class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def display(self):
        print(f"The name of the student is {self.name} and the marks scored is {self.marks}")

        if(self.marks>=40):
            print("pass")
        else:
            print("fail")


# Creating objects
s1 = Student("Vengatesh", 92)
s2 = Student("Rahul", 78)

# Calling methods
s1.display()
s2.display()