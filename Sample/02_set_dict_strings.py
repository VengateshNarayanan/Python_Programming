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

a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

print(a | b)  # Union: {1, 2, 3, 4, 5, 6}
print(a & b)  # Intersection: {3, 4}
print(a - b)  # Difference: {1, 2}
print(a ^ b)  # Symmetric difference: {1, 2, 5, 6}

values = [1, 2, 2, 3, 3, 4]

unique_values = list(set(values))
print(unique_values)