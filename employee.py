class emp:
    def __init__(self , name , salary):
        self.name = name
        self.salary = salary


    def display(self):
        print("Name: " , self.name)
        print("salary: " , self.salary)

        if(self.salary>=50000):
            print("high salary")
        else:
            print("low salary")

s1 = emp("Vengatesh" , 67000)
s2 = emp("vedant sane" , 78000)
s3 = emp("ralhul" , 43000)


s1.display()
s2.display()
s3.display()
        