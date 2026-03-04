#Let's learn to take inputs from the user.
a=input("Enter your name:") #result for this is always string
b=int(input("Enter your age:")) #to take input values
print("Hi there! Welcome",a,".Ohh! so you're",b,"years old")

#Let's practice some questions. WAP to input 3 numbers and print their sum.
x=float(input("Enter a number:"))
y=float(input("Another number:"))
z=float(input("third number:"))
print("Sum is:",x+y+z)
print("Average:",(x+y+z)/3)

#WAP to input side of a square and print its area.
l=float(input("Enter the side length of a sq."))
print("Area is:",l*l) #or it can be written as,"l**2", which means l to the power 2.


#WAP to input 2 numbers and print true if a is greater than or equal to b. if not false. 
first=float(input("Enter first number:"))
second=float(input("Second number:"))
print(first>=second)