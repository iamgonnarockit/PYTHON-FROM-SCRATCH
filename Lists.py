#Lists in Python: A built-in data type that stores set of values.
#It can store elements of different types(integer, float, string,etc)
#Note: Lists in Python is mutable i.e it can be changed but strings is immutable i.e unchangeable
marks=[20,90,47,94]
print(marks[0])
marks[1]=45 #here the marks is changed
print(marks[1])
print(len(marks))

#List Slicing - accessing a part of lists
print(marks[0:3]) #ending is not included
print(marks[-3:-1]) #negative slicing same as strings

