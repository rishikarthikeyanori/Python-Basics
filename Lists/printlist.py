list=[]
n=int(input("enter the elements of the list: "))
for x in range(0,n+1):
    list.append(input("enter the element :"))

rev=[]
    
for i in range(len(list)-1,-1,-1):
    rev.append(list[i])

print[rev]

# print the output in the form of a list