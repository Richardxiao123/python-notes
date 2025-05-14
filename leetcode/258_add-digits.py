class Solution:
    def addDigits(self, num: int) -> int:
        nums=num
        while len(str(nums))>1:
            temp=0
            for i in range(len(str(nums))):
                temp+=int(str(nums)[i])
            nums=temp
        return nums
        
