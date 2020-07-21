def sum(nums):
    for i in range(len(nums)):
        minpos=i
        for j in range(i,len(nums)):
            if nums[j]<nums[minpos]:
                minpos=j
        temp=nums[i]
        nums[i]=nums[minpos]
        nums[minpos]=temp


nums=[1,4,6,2,3,9,7,8]
sum(nums)
print(nums)
