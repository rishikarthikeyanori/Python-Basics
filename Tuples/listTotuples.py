n = int(input("Enter the number of elements: "))

lst = []

for i in range(n):
    num = int(input("Enter a number: "))
    lst.append(num)

t = tuple(lst)

print(t)