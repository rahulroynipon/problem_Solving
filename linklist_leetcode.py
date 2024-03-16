class Slotion:
    def findPeak(self,nums):
        n = len(nums)-1
        if n==0:
            return 0
        if nums[n]>nums[n-1]:
            return n

        for i in range(1,n):
            if nums[i-1]<nums[i]>nums[i+1]:
                return i
        

        return 0


        



x = Slotion()

print(x.findPeak([1,3,2]))