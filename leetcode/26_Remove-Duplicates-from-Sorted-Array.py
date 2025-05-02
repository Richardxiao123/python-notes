class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        dif_nums = 1
        cur_nums = nums[0]
        for i in range(1, len(nums)):
            if nums[i] != cur_nums:
                nums[dif_nums] = nums[i]
                cur_nums = nums[i]
                dif_nums += 1
        return dif_nums
