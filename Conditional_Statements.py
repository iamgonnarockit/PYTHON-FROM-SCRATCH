#Let's learn about conditional statements. 
#WAP to check whether the canditate is eligible for voting or not. 
  
age=int(input("Enter your age:"))
if(age>=18):
    print("Eligible")
else:
    print("Not Eligible")

#WAP for traffic lights.
lights=input("Which color of light do you see? \n")
if(lights=="Red"):
    print("-STOP")
elif(lights=="Yellow"): #elif is basically else if.
    print("LOOK")
else:
    print("GO")


