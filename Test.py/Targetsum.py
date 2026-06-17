#  Find All Pairs With Target Sum
# nums = [2, 7, 11, 15, 3, 6], target = 9
# # Output:
# # (2,7)
# # (3,6)

#take input
#2+7
# 2+11
# 2+15
# 2+3
# 2+6
# 7+2 , if a+b and b+a = target , print either a,b or b,a
# 7+7
# 7+11........

nums = [2, 11, 7, 15, 3, 6]
target=9
sum=0
list=[]
for i in range(0,len(nums)):
    for j in range(i+1,len(nums)):
        sum=nums[i]+nums[j]
        if sum==target:
            list.append([nums[i],nums[j]])
print(list)

            
        
