# #WAP to check if a list contains a palindrome of elements. 

movies=[]
print("Hey Students!! Let's get to know ya'll 3 favourite movies today")
mov1=input("First fav:")
mov2=input("Second fav:")
mov3=input("Third fav:")

movies.append(mov1) #adds to the list
movies.append(mov2)
movies.append(mov3)
cpy=movies.copy()
cpy.reverse()
if movies==cpy:
    print("Yes")
else:
    print("No")


    #Or we can use slicing. 

movies = []
print("Hey Students!! Let's get to know ya'll 3 favourite movies today")
mov1 = input("First fav: ")
mov2 = input("Second fav: ")
mov3 = input("Third fav: ")

movies.append(mov1)
movies.append(mov2)
movies.append(mov3)

if movies == movies[::-1]:  # slicing creates a reversed copy without modifying original
    print("Yes, it's a palindrome!")
else:
    print("No, it's not a palindrome.")