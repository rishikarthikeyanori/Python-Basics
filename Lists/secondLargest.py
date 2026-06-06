size = int(input("Enter the number of elements: "))

a = []
for i in range(size):
    num = int(input("Enter a number: "))
    a.append(num)

if a[0] > a[1]:         #3,8,6,5,4
    largest = a[0]
    second = a[1]
else:
    largest = a[1]#largest=8
    second = a[0]#3

for i in range(2,len(a)):#2,3
    num=a[i]#a[2]=6,a[3]=5
    if num > largest:
        second = largest
        largest = num
    elif num > second and num != largest:#second=6
        second = num

print("Second largest Of the list =", second)