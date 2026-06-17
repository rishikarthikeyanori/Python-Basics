# Given an array of integers nums and an integer target, return the indices i and j such that nums[i] + nums[j] == target and i != j.
# nums = [3,4,5,6], target = 7
# Output: [0,1]

nums=[3,4,5,6]
target=7
sum=0
for i in range(0,len(nums)):
    for j in range(i+1,len(nums)):
        sum=nums[i]+nums[j]
        if sum==target:
            print([i,j])

