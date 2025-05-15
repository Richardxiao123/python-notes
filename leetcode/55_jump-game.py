class Solution:
    def canJump(self, nums: List[int]) -> bool:
        goal=len(nums)
        walk=nums[0]
        if nums==[0]:return True
        for i in range(len(nums)):
            if walk<=0:return False
            walk-=1

            if nums[i]>walk:
                walk=nums[i]

            
        return True
