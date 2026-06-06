t = (1, 2, 2, 3, 4, 4, 5)

lst = []

for x in t:
    if x not in lst:
        lst.append(x)

result = tuple(lst)

print(result)