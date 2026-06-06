
a=[]
n=int(input("enter the number of elements: "))
for i in range(n):
    a.append(int(input("enter the elements: ")))
sum=0
for i in range(0,len(a)):
    num=a[i]
    sum+=num
print(sum)

avg=sum/len(a)
print(avg)