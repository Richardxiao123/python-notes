class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(len(nums)):
            cur=i
            while i<len(nums)-1 and nums[i]==0:
                i+=1
            a=nums[cur]
            nums[cur]=nums[i]
            nums[i]=a
