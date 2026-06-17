student = {
    "name": "Rishi",
    "age": 18,
    "branch": "CSE"
}

key = input("Enter the key to search: ")

if key in student:
    print("Key found")
    print("Value =", student[key])
else:
    print("Key not found")