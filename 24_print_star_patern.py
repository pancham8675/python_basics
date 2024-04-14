
# Print the star pattern

num=int(input("Enter a number: "))

#1
for i in range (1,num+1):
    print("*"*i)

print(" ")

#2
for i in range (num):
    print(" "*(num-i-1), end=" ")
    print("*"*(2*i+1), end=" ")
    print(" "*(num-i-1))

print(" ")

#3
for i in range (num):
    print("*"*(num-i))

numb=int(input("Enter a number: "))
for i in range (numb):
    print(" "*(numb-i-1), end=" ")
    print("*"*(2*i+1), end=" ")
    print(" "*(numb-i-1))
