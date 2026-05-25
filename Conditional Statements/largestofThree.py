# 3. Largest of Three Numbers
# Take 3 numbers and print the largest number

a=int(input("enter the number 1: "))
b=int(input("enter the number 2: "))
c=int(input("enter the number 3: "))#take input from user 
if a>b and a>c:#condition for a greatest number
    print("largest number is a=",a)
elif b>a and b>c:# condition for be greatest number
    print("largest number is b=",b)
else:#condition for c greater number
    print("largest number is c=",c)