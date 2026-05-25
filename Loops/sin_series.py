# # Write a program to find the sum of n terms of the sin series sin(x) = x - x3 + x5 – x
# #  7
# # (−1)**n((x**(2*n+1))/(2n+1)!)​

# # step 1: take user input
# # step 2: initialize sum to 0
# # step 3: take for loop from 0,n
# # step 4: sum = the n terms sin series formula 
# # step 5: print sum

import math#imported math libarary so that we could use factorial function
x=int(input("enter the number which is to be substituted in the eqn: "))#took the number which is to be substituted in the eqn
num=int(input("enter the value of n for which sum series is to be calculated: "))#took the actual number of values to be printed
term,sum=0,0#initialized the term and sum variables to 0 in order to avoid garbage values
for i in range (1,num+1):#took range as 1,n+1 because 0th value in sinx series does not exist
        term=((-1)**i * (x**(2*i+1))) / math.factorial(2*i+1)#formula for sinx series 
        sum+=term#assigned value of term to sum and kept adding the value of term to sum
print (sum)#printing sum outside the loop since we do not want the value after every iteration