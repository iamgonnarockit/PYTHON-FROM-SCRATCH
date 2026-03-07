#Methods of Lists
Countries=["Nepal", "India", "China", "Bhutan", "Laos", "Afghanistan"]
print("Length of the given lists is",len(Countries))

Countries.append("USA") #adds one item to the list
print(Countries)

Countries.sort( ) #Sort in ascending order
print(Countries)

Countries.sort(reverse=True) #Sort is descending order if it's true and ascending if false.
print(Countries)

Countries.reverse #this executes the original string. 
print(Countries)

Countries.insert(1,"Vietnam") #adds new value to the mentioned index
print(Countries)

Countries.remove("Vietnam") #removes first occurrence of the element
print(Countries)

Countries.pop(3) #removes element at given index
print(Countries)