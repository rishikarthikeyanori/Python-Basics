# Program to print the Nth prime number

n = int(input("Enter the value of N: "))

count = 0
num = 2

while True:
    prime = True
    for i in range(2, num):
        if num % i == 0:
            prime = False
            break

    if prime:
        count += 1
        if count == n:
            print(f"The prime number is:", num)
            break
    num+=1