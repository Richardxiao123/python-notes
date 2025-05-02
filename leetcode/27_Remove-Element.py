class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        dif_val_cnt=0
        for i in range(len(nums)):
            if nums[i] !=val:                
                nums[dif_val_cnt]=nums[i]
                dif_val_cnt+=1
        return dif_val_cnt

