list=[1,4,6,7]
max=list[0]
min=list[0]
for i in range(len(list)):
    if list[i]>max:
        max=list[i]
    
    if list[i]<min:
        min=list[i]
    
print("the max value of the list is: ",max)
print("the min value of the list is: ",min)