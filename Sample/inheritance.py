class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def display_details(self):
        print("Name:", self.name)
        print("Salary:", self.salary)


class Manager(Employee):
    def __init__(self, name, salary, department):
        super().__init__(name, salary)
        self.department = department

    def display_department(self):
        print("Department:", self.department)


# Create an object
m = Manager("Rahul", 50000, "IT")

# Call methods
m.display_details()
m.display_department()