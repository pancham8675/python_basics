#Set is a collection of non repetitive elements
#The below syntax will create an empty dictionary and not an empty set
a={}
print(type(a))

#The below syntax will create an empty set
b=set()
print(type(b))

#Adding values to an empty set
b.add(3)
b.add(54)
b.add(67)
# b.add({4:6}) #Cannot add list or dictionary in sets as it is hashable

print(b)
print(len(b)) #Prints length of set b

b.remove(3) #Removes 3 from set b
b.pop() #Removes a random element from set b

print(b)




