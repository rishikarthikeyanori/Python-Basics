# Given an integer array nums, return true if any value appears more than once in the array, otherwise return false.
# nums = [1, 2, 3, 3], Output: true

num = [2, 7, 11, 15, 3, 3]
res=False
for i in range(0,len(num)):
    for j in range(i+1,len(num)):
        if num[i]==num[j]:
            res=True
        else:
            res=False

if res==True:
    print("true , elements in the given list are repeating")
else:
    print("false, elements in the list are not repeating")
            