s=input("enter the desired character: ")
count=0
for wrds in s.split(): 
    if len(wrds)%2==0:
        print(wrds,end=' ')
        count+=1
print()        
    
        
print("the number of even letter words given in this string are: ",count)
print()
        
    
    
    
