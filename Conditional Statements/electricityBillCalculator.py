# 5. Electricity Bill Calculator
# Calculate bill based on units.
# Conditions
# First 100 units → ₹2/unit
# Next 100 units → ₹3/unit
# Above 200 → ₹5/unit

units=int(input("enter the number of units"))
if units<=100:
    print("the bill =",2*units)
elif units<=200:
    
    print("the bill =",100*2+(units-100)*3)
else :
    print("the bill =",100*2+100*3+(units-200)*5)