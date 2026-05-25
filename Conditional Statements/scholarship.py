# A student gets scholarship only if:
# Attendance >= 75
# AND marks >= 85
# Conditions
# First check attendance
# If attendance valid, check marks
# Else print “Not Eligible due to Attendance”

attend=int(input("enter the students attendance"))
if attend>=75:
    marks=int(input("enter the studets marks"))
    if marks>=85:
        print("eligible for scholarship")
    else:
        print("not eligible due to marks")
else:
    print("not eligible for scholarsip due to attendance")   