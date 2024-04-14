
# Find factorial
def factorial(num):
    factorial=1
    for i in range (1,num+1):
        factorial=factorial*i
    return factorial

f = factorial(3)
print(f)


# Find the geatest number
def greatest(num1,num2,num3):
    if(num1>num2):
        if(num1>num3):
            return num1
        else:
            return num3
    else:
        if(num2>num3):
            return num2
        else:
            return num3

g = greatest(21,34,56)
print(g)


# Celcius to farenheit converter
def farh(cel):
    return ((cel * (9/5)) + 32)

f=farh(23)
print(f)