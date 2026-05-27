
# Write a program to generate the multiplication table for n numbers up to k terms (nested
# loops). 

num=int(input("enter the number: "))
for i in range(1,num+1):
    for j in range(1,num+1):
        print (num,end=' ')
        num=num*i
    print()
    break
