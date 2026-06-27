s1=input("enter the string: ")
s2=input("enter the 2nd string: ")
result=False
if len(s1.strip())!=len(s2.strip()):
    print("not an anagram")
for ch in s1.strip():
    if ch in s2.strip():
        result=True
    else: 
        result=False
        break
        
if result==True:
    print("given strings are anagrams")
else:
    print("given strings are not anagrams")



# #listen == silent
# #for every character in string 1 
# #1st iteration =l
# # s2 lo l undha 
# #okavela unte anagram for that iteration






