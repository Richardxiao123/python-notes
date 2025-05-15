class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n=len(nums)
        nums.sort()
        
        for i in range(n):
            if i != nums[i]:
                return i
        return nums[-1]+1
