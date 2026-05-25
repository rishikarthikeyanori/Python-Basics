# Create a college admission checker using nested if statements.
# Conditions
# Student must have:
# 70% or above in 12th
# If eligible:
# Check entrance exam rank
# If rank is below 5000:
# Student gets seat
# Then check family income:
# If income < 500000 → Scholarship Eligible
# Else → No Scholarship
# If rank above 5000:
# No Seat Allotted
# If marks below 70:
# Not Eligible for Admission

marks=int(input("enter 12th grade marks: "))
if marks>=70:
    rank=int(input("enter the entrance exam rank"))
    if rank<5000:
        print("seat allotted")
        income=int(input("enter the family income"))
        if income<500000:
            print("eligible for scholarship")
        else:
            print("ineligible for scholarship")
    else:
        print("seat not allotted due to rank")
else:
    print("seat not allotted due to 12th marks")