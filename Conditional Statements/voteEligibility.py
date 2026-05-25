# 2. Take age as input and check whether the person can vote.
# Conditions
# Age >= 18 → Eligible
# Else → Not Eligible

num=int(input("enter the age: "))#take input from user 
if num<18:#condition under 18
    print("ineligible to vote")
else:#condition for ages 18 and above
    print("eligible to vote")