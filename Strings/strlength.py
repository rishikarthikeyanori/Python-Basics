# Write a program to find the string length of a string without using the predefined function. 
s=input("enter the characters: ")
count=0
for ch in s.strip():
    if ch==" ":
        continue
    count+=1
    
    
print(count)