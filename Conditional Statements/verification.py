# 7. Login + OTP Verification System
# Create a mini authentication system.
# Requirements:
# Ask username
# Ask password
# If both correct:
# Ask OTP
# If OTP correct → Login Successful
# Else → Invalid OTP
# If username/password wrong → Invalid Credentials

sysusername="rishi"
syspassword=12345
sysotp= 2468

username=input("enter the username")
password=int(input("enter your password"))

if username==sysusername and password == syspassword:
    otp=int(input("enter the correct otp"))
    if otp==sysotp:
        print("login successful")
    else:
        print("enter the correct otp")
else:
    print("enter the correct credentials")  