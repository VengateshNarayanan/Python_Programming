# Parent class
class person:
    def __init__(self , name , age):
        self.name = name 
        self.age = age

    def display_info(self):
        print(f"Name:{self.name} , Age:{self.age}")

    #child class 
class student(person):
    def __init__(self , name , age , student_id):
        super().__init__(name , age)
        self.student_id = student_id

    def display_student_info(self):
        self.display_info()
        print(f"Student ID: {self.student_id}")

student1 = student("Sarvesh" , 20 , "125AX047")
student1.display_student_info()