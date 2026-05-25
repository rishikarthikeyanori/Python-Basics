#  ATM Withdrawal System
# A user has ₹10,000 balance.
# Conditions
# Withdrawal amount must be multiple of 100
# Cannot exceed balance
# Otherwise deduct and print remaining balance

balance=10000
amount=int(input("enter amount required for withdrawal:"))
if amount >balance:
    print("insufficient funds")
elif amount <=0:
    print("enter valid amount")
elif amount%100==0:
    balance = balance-amount
    print("amount recieved and balance left is:",amount ,balance)
else :
    print("enter a valid number in multiple of 100")