# Write a program to convert the decimal number into
# binary to decimal. Ex: 1101 = 1*2 3 + 1 * 2 2 + 0 *
# 2 1+ 1* 2 0 =13 
#step 1: take user input
#step 2: find the length of the binary number
#step 3: use for loop to find from the range of 0 to length of the binary number
#step 4: find the last digit of the binary number and store it in a variable
#step 5: find the decimal value of the last digit and add it to the reverse variable   
#step 6: remove the last digit from the binary number
#step 7: print the reverse variable outside the for loop

num=int(input("Enter a number: "))
i=len(str(num))
rev,dig=0,0
for i in range(0,i):
    dig=num%10
    rev=rev+(dig* 2**i)
    num=num//10
print(rev)