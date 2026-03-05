#String is a data type that stores a sequence of characters.
#Basic Operations of string
#1. Concatenation
a="Sad"
b="ikshya"
print(a+b)

#2. Length of string - finds the number of characters used in string
print("This word consists total of",len(a+b),"characters")

#Slicing in string- It means accessing parts of a string. This is very important in ML.
#Note: str[ :4] is same as str[0:4]. str[1: ] is same as str[1: len(str)]
#Negative Index: Negative indexing in Python is a method for accessing elements in a sequence (like a list, tuple, or string) by counting backward from the end. 
# The last element is accessed using an index of -1, the second-to-last is -2, and so on.
str="Technology"
print(str[1:5])

fruits=["Apple","Blueberry","Orange","Pineapple","Mangoes"]
print(fruits[-1])
print(fruits[:-2])

#String Functions
str="i want to be fluent in Python"
print(str.capitalize( )) #Capitalizes the first letter
print(str.endswith("on")) #Returns tru if string ends with substr
print(str.replace("n","p")) #replaces all occurrences of old with new
print(str.count("o")) #counts the occurrence of substr in string
print(str.find("in"))
