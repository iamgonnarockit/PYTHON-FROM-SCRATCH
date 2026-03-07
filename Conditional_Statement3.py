#WAP to find the greatest among 3 entered numbers
num1=float(input("1st Number:"))
num2=float(input("2nd Number:"))
num3=float(input("3rd Number:"))
if(num1>num2 and num1>num3):
    print(num1,"is the greatest")
elif(num2>num1 and num2>num3):
    print(num2,"is the greatest")
else:
    print(num3,"is the greatest")

#WAP to check if the entered number is multiple of 7.
num=int(input("Enter any number:"))
if(num%7==0):
    print(num,"is multiple of 7")
else:
    print(num,"is not a multiple of 7")