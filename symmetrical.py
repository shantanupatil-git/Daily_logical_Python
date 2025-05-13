#Write a Python program to test whether a given number is symmetrical or not.
#A number is symmetrical when it is equal of its reverse.

#hard coded values

def symmerical(number):
    num = str(number) #str(number) = convert number to string.
    reversed=num[::-1] #revered the given list
    return num == reversed

print(symmerical(121)) #TRUE
print(symmerical(234)) #FASLE

#user input

def symmerical(number):
    num = str(number)
    reversed = num[::-1]
    return num == reversed
user = int(input("ENTER A NUMBER"))
if symmerical(user):
    print("ITS AN SYMMERICAL NUMBERS")
else:
    print("ITS NOT AN SYMMERICAL NUMBERS")