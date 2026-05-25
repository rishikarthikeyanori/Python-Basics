# Write a program to check whether the given number is Armstrong or not. An Armstrong
# number of three digits is an integer such that the sum of the cubes of its digits is equal to the
# number itself. For example, 371 is an Armstrong number since 33 + 73 + 13 = 371.
# step 1: take user input
# step 2:extract the last digit of the number by doing n%10
# step 3: build the reverse number by doing rev take the last digit by doing n%10 =rev + (last digit)^3
# step 4: divide the number by 10
# step 5: if the reversed number is equal to the original given number then it is an armstrong number
# step 6: else print not an armstrong number 

n=int(input("enter the number"))#371,37,3
rev,dig=0,0
temp=n
while n>0:
    dig=n%10#1,7,3
    rev=rev+(dig**3)#rev=0+1^3=1,rev=1+7^3=344,rev=344+3^3
    n=n//10#37,3,0
if temp==rev:
    print ("the given number is an armstrong number")
else:
    print("the given number is not an armstrong number")