# *****
# ****
# ***               inverted right half 
# **
# *


n=int(input("enter the number of rows to print: "))
for i in range(n,0,-1):
    for j in range(1,i+1):
        print("*",end='')
    print()