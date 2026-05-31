s=str(input("enter the characters: "))
vow,con=0,0
for ch in s:
    if ch=="a" or ch=="e" or ch=="i" or ch=="o" or ch=="u":
        vow+=1
        
    else:
        con+=1
    
print(con,"is the number of consonants in this string")
print(vow,"is the number of vowel in this string")
