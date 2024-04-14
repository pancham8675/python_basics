
# Concatenating two strings

greeting="Good Morning "
name= input("Enter name: ")
c= greeting + name + "!"
print("Good Afternoon "+ name )
print(c)

# String Slicing
name="Pancham"
print(name[4]) # Prints index value of 4
print(name[2:5]) #Prints from index 2 to 5
print(name[2:]) # Nothing is assumed as end
print(name[:5]) #Nothing is assumed as zero
print(name[1:6:2]) #{From:To: Skip number}