###-----------------------Strings-----------------------###

# text = "  python programming  "

# text = text.strip().upper()
# print(text)

# sentence = "Python is powerful"
# words = sentence.split()

# print(words)

# join is used to join the separated strings

# formatting
# name = "Venky"
# marks = 92.5

# print(f"{name} scored {marks:.1f} marks.")

# text = "programming"

# print("gram" in text)  # True

# for char in text:
#     print(char)

###-------------------SETS------------------###

# a = {1, 2, 3, 4}
# b = {3, 4, 5, 6}

# print(a | b)  # Union: {1, 2, 3, 4, 5, 6}
# print(a & b)  # Intersection: {3, 4}
# print(a - b)  # Difference: {1, 2}
# print(a ^ b)  # Symmetric difference: {1, 2, 5, 6}

# values = [1, 2, 2, 3, 3, 4]

# unique_values = list(set(values))
# print(unique_values)


###-----------DICTIONARY------------###
# student = {
#     "name": "Venky",
#     "age": 20,
#     "branch": "CSE-IOT"
# }
# print(student)
# print(student["name"])
# print(student.get("marks", 0))

# student["marks"] = 90
# student["age"] = 21
# student.pop("age")
# print(student)

student = {"name": "Venky", "age": 20, "marks": 90}

for key in student:
    print(key, student[key])

squares = {x: x**2 for x in range(1, 6)}
print(squares)
