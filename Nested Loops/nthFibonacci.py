# Program to print Fibonacci numbers in a given range

start = int(input("Enter the starting range: "))
end = int(input("Enter the ending range: "))

a, b = 0, 1

print("Fibonacci numbers in the given range are:")

while a <= end:
    if a >= start:
        print(a, end=" ")
    temp=b
    b=a+b
    a=temp