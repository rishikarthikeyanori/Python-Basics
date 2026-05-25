# Write a program to reverse a given number
# Ex: 1234 reverse=4*10 3 +3 * 10 2 + 2 * 10 1 + 1 * 10 0 =4321 
# step 1: take the number from the user.
# step 2: extract the last digit from the number by using %
# step 3: initialize the rev number to 0 
# step 4: add the last digit*10 to this reversed number
# step 5: build a reverse number by using the formula rev=rev+dig*10
# step 6: divide the number by 10 to get rid of the last digit of that number for next iteration
# step 7: print reversed number

num=int(input("enter any number: "))#num=1234,num=123,num=12,num=1
rev,dig=0,0
while num>0:
    dig=num%10 #dig=4,dig=3,dig=2,dig=1
    rev=rev*10+dig#rev=0*10+4=4,rev=4*10+3=43,rev=43*10+2=432,rev=432*10+1=4321
    num=num//10# num=1234//10=123,num=12,num=1,num=0
print(rev)
