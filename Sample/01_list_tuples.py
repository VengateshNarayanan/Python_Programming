# ------------------LISTS OPERATIONS-----------------#
# list1 = [1, 2, 3]
# list2 = [4, 5, 6]


#  join = [list1 + list2]
# print(join)

# list = [1,2,2,3,4,5,5]

## swapping 2 lists
# items = [10, 20, 30, 40, 50]
# swap = items[0]
# items[0] = items[4]
# items[4] = swap
# print(items)

# items.remove(30)
# print(items)

## concatenation
# l1 = ['banana' , 'apple' , 'mango' , 'apple']

# l2 = l1 + [2,4,54,6,67]
# print(l2)

# l1.append(34)
# print(l1)

# l1.insert(0 , 60)
# print(l1)

# l1.remove('banana')
# print(l1)

# l2 = l1.count("apple")
# print(l2)

# Key properties:
# - Ordered: elements retain their positions.
# - Mutable: elements can be modified.
# - Allows duplicates.
# - Supports indexing and slicing.
# - Can contain nested lists.

# Essential list methods
# Method	Purpose
# append(x)	Adds one element at the end
# extend(iterable)	Adds multiple elements
# insert(i, x)	Inserts an element at an index
# remove(x)	Removes the first matching value
# pop(i)	Removes and returns an element
# clear()	Removes all elements
# index(x)	Returns the first matching index
# count(x)	Counts occurrences
# sort()	Sorts the original list
# reverse()	Reverses the original list
# copy()	Creates a shallow copy



# --------------------TUPLES OPERATIONS----------------=#

#  PROPERTIES 
# Ordered  , immutable , and allow duplicates

## slicing and indexing
# data = (10, 20, 30, 40)

# print(data[0])       # 10
# print(data[1:3])     # (20, 30)
# print(data.count(20))
# print(data.index(30))

# a = (10)    # int
# b = (10,)   # tuple

# tupple unpacking
student = ("Vengatesh", 20, "CSE-IOT")

name, age, branch = student

print(name)
print(age)
print(branch)

# extended unpacking
first, *middle, last = (10, 20, 30, 40, 50)

print(first)   # 10
print(middle)  # [20, 30, 40]
print(last)    # 50