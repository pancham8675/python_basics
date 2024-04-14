
# f=open("sample.txt","r") #Opens the file
# # data=f.read() #Reads the data in the file
# # data=f.read(6) #Reads the first 6 characters of the file
# data = f.readline() #Reads the first line of the file
# print(data) #Printing the data in the file

# data = f.readline() #Reads the Second line of the file
# print(data)

# data = f.readline() #Reads the Third line of the file
# print(data)

# f.close() #Closes the file


f=open("another.txt", "w")
f.write("\nPlease write this to the file")
f.close()

f=open("another.txt", "a")
f.write("\nI am appending")
f.close()

f=open("sample.txt","r")
data = f.read()
if "gulabi" in data:
    print("Gulabi is present")
else:
    print("Gulabi is not present")
