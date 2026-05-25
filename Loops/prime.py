# Write a program to find whether the given number is prime or not.
# step 1: take user input
# step 2: check if given number is 0 and 1
# step 3: if it is 0 or 1 then write neither prime not composite
# step 4: for prime case you have to divide by the range of i
# step 5: take the range of i from 2 (because 0 and 1 is already covered)
# step 6: if any number in the i range divides the given number then the number is composite
# step 7: if no number in the i range divides the given number then the number is prime

num=int(input("enter the number: "))

if num==0 or num==1:
    print("the number is neither prime nor composite")

else:
    flag = True
    for i in range(2,num):
        if num%i==0:
            flag=False
            break

    if flag==False:
        print("the number is composite")
    else:
        print("the number is prime")