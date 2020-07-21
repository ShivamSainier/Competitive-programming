def sum(nums):
    for i in range(len(nums)-1,0,-1):
        for j in range(i):
            if nums[j]>nums[j+1]:
                nums[j],nums[j+1]=nums[j+1],nums[j]
    return nums


nums=[1,4,2,8,5,0,9,10,13,12]
sum(nums)
print(nums)

