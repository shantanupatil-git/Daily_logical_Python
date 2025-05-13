#hard code values
a = 0
b = 1
print(a)
print(b)
for i in range (2,10):
    c = a+b
    a = b
    b = c
    print(c)
#a=0 b=1 c=0+1->1
#a=1 b=1 c=1+1->2
#a=1 b=2 c=1+2->3......still 10 values.

