#     *
#    ***
#   *****               full pyramid pattern 
#  *******
# *********


num=int(input("enter the number of rows: "))
for i in range (1,num+1):
    for j in range(1,num-i+1):
        print(" ",end='')
    for j in range(1,2*i):
        print ("*",end='')
    print()
