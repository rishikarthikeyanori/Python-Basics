# Write a program to print the Fibonacci number.
# Hint: (Fibonacci series is 0, 1, 1, 2, 3, 5, 8,)

a,b=0,1
for i in range (a,20):
    print(a)
    temp=b
    b=a+b
    a=temp