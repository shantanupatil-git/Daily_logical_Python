for num in range(3, 30): #Range
    prime = True #flag
    for i in range(2, num):
        if(num % i == 0):  # Check if num is divisible by i
            prime = False #flag
            break
    if(prime):
        print(num)
