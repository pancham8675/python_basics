
dict = {
"pancham": 19,
"hello": "world",
"anotherdict": {"player": "Messi"}
}

# Dictionary Methods
print(list(dict.keys())) #prints the keys in the dictionary in list format
print(list(dict.values())) #prints the values in the dictionary in list format

dict1={
    "grand":"entry"
}
dict.update(dict1) #Updates dictionary by adding the key-value pairs from dict1
print(dict)

print(dict.get("hello")) #Prints value associated with key "hello"
print(dict["hello"]) #Prints value associated with key "hello"

# The difference between .get and [] syntax in dictionaries:
print(dict.get("hello1")) #Returns None if the key is not present in the dictionary
print(dict["hello1"]) #Throws an error if the key is not present in the dictionary
