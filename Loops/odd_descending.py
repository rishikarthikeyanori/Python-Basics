# Write a program to take N as input and print the odd numbers in descending order. 

n=int(input("enter the value for n: "))
for i in range (n,0,-1):
    if i%2!=0:
        print(i)