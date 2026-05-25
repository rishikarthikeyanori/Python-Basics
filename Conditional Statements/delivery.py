# Create a food delivery condition system.
# Conditions
# Restaurant should be open
# If open:
# Check if item is available
# If item available:
# Check if balance is enough
# If balance enough:
# Order Successful
# Else print proper error message

restaurant=True
item=True
balance=5000

if restaurant==True:
    if item==True:
        num=int(input("eter the price of item"))
        if num<=balance:
            print("order item")
        else:
            print("cannot order item")
    else:
        print("item does not exist")
else:
    print("restauarant is closed")

    