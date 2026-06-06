t = (10, 45, 67, 89, 23, 78)

largest = t[0]
second = t[1]

if second > largest:
    largest, second = second, largest

for i in range(2,len(t)):
    num=t[i]
    if num > largest:
        second = largest
        largest = num
    elif num > second and num != largest:
        second = num

print("Second largest:", second)