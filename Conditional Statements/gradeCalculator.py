# 4. Grade Calculator
# Take marks as input and print grade.
# Conditions
# 90+ → A
# 75–89 → B
# 50–74 → C
# Below 50 → Fail

marks=int(input("enter the marks of the student: "))
#take input from user
if marks<=0 and marks>=100:
    print("enter valid marks")
#define range 
if marks>=90 and marks<100:
    print("Grade A")
elif 75<=marks<=89:# condition for be greatest number
    print("Grade B")
elif 50<=marks<=74:#condition for c greater number
    print("Grade C")
else:
    print("Fail")