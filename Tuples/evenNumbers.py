t = (12, 15, 18, 21, 24, 27)

count = 0

for num in t:
    if num % 2 == 0:
        count += 1

print("Number of even elements:", count)