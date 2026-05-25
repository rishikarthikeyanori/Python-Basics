# sum of digits in a number using while loop
# step 1: take user input
# step 2: initialize sum to 0 to avoid garbage values
# step 3: keep whlie condition as num greater than 0
# step 4: extract last digit
# step 5: add the last digit to the reversed number
# step 6: print the sum of the reversed number or print reversed


num=int(input("enter the number: "))
rev,dig=0,0
while num>0:
    dig=num%10
    rev=rev+dig
    num=num//10
print(rev)
    
