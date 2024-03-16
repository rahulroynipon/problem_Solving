def remove(nums):

    prev = 0
    n = len(nums)
    i = 1
    while i<n:
        if nums[i]:
            for i in range(i,n):
                if nums[i]>nums[prev]:
                    nums[prev+1] = nums[i]
                    nums[i] = ''
                    prev+=1
                    break
                else:
                    nums[i] = ''
            

        i+=1

    return prev+1


print(remove([0,0,1,1,1,2,2,3,3,4]))