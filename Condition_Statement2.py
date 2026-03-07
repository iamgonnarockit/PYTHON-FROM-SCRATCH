#WAP to calculate the grade of students given their marks.
Marks=float(input("Enter your marks:"))
if(Marks>90 and Marks<=100):
    print("Grade=A+")
elif(Marks>80 and Marks<=90):
    print("Grade = A")
elif(Marks>70 and Marks<=80):
    print("Grade = B+")
elif(Marks>60 and Marks<=70):
    print("Grade = B")
elif(Marks>50 and Marks<=60):
    print("Grade = C+")
elif(Marks>40 and Marks<=50):
    print("Grade = C")
else:
    print("Fail")
    